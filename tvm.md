## TVM

> Relay 是 TVM 中用来替代 NNVM 的模块，其本身被认为是 NNVM 第二代。 
>
>  https://zhuanlan.zhihu.com/p/91283238 

### 安装 LLVM

#### Debian/Ubuntu

方法1：

```shell
$ #(optinal) apt-add-repository deb ... # https://apt.llvm.org/
$ apt update
$ apt install llvm-6.0 llvm-6.0-dev llvm-6.0-runtime
```

方法2：

```shell
$ bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
```

Fix `lsb_release: command not found`

```shell
$ apt update && apt install lsb-core
```

#### 源码编译

 http://releases.llvm.org/download.html 

 http://llvm.org/docs/CMake.html 

```shell
$ cd path/to/llvm-src
$ mkdir build && cd build
$ cmake ../
$ cmake --build .
$ cmake --build . --target install # if install to system
```

 No CMAKE_CXX_COMPILER could be found 

```shell
$ apt install build-essential
```

### 编译 TVM

```shell
$ git clone --recursive https://github.com/apache/incubator-tvm
$ cd tvm && mkdir build
$ cp cmake/config.cmake build
$ cd build
$ vi config.cmake # edit options: LLVM, CUDA, etc. 
$ cmake ..
$ make -j4
```

 https://docs.tvm.ai/install/from_source.html 

### 安装 TVM 到 Python

方法1：

```shell
$ export TVM_HOME=/path/to/tvm
$ export PYTHONPATH=$TVM_HOME/python:$TVM_HOME/topi/python:$TVM_HOME/nnvm/python:${PYTHONPATH}
```

方法2：

```shell
$ cd /path/to/tvm
$ cd python; python setup.py install --user; cd ..
$ cd topi/python; python setup.py install --user; cd ../..
$ cd nnvm/python; python setup.py install --user; cd ../..
```

Dependencies

- Necessary `pip3 install --user numpy decorator attrs`
-  RPC Tracker `pip3 install --user tornado`
-  auto-tuning module `pip3 install --user tornado psutil xgboost`
-  build tvm to compile a model `sudo apt install antlr4; pip3 install --user mypy orderedset antlr4-python3-runtime`

TVMError: Check failed: bf != nullptr: Target llvm is not enabled

>  cmake automatically identify LLVM path. In your case you can set the llvm-config path manually in `build/config.cmake` as below: `set(USE_LLVM /usr/lib/llvm-6.0/bin/llvm-config)` 

nvcc not found

```shell
$ export PATH=/path/to/cuda/bin:$PATH
```

### 深度学习模型编译和调优（Python）

Python API:  https://docs.tvm.ai/api/python/index.html 

tuning functions

```python
import tvm
from tvm import relay
from tvm.relay import testing
from tvm.autotvm.tuner import XGBTuner, GATuner, RandomTuner, GridSearchTuner
from tvm.autotvm.graph_tuner import DPTuner, PBQPTuner
import tvm.contrib.graph_runtime as runtime
import numpy as np
import timeit
from tvm.contrib import util
import nnvm


def tune_tasks(option):
    print('Creating tasks ...')
    tasks = autotvm.task.extract_from_program(mod["main"], 
                                                target=target,
                                                params=params, 
                                                ops=(relay.op.nn.conv2d, 
                                                     relay.op.nn.dense))
    if option['try_winograd']:
        for i in range(len(tasks)):
            try:  # try winograd template
                tsk = autotvm.task.create(tasks[i].name, 
                                          tasks[i].args,
                                          tasks[i].target, 
                                          tasks[i].target_host, 'winograd')
                input_channel = tsk.workload[1][1]
                if input_channel >= 64:
                    tasks[i] = tsk
            except Exception as err:
                print(err)

    # create tmp log file
    tmp_log_file = option['log_file']
    if os.path.exists(tmp_log_file): os.remove(tmp_log_file)

    for i, tsk in enumerate(reversed(tasks)):

        # converting conv2d tasks to conv2d_NCHWc tasks
        # op_name = tsk.workload[0]
        # if op_name == 'conv2d':
        #     func_create = 'topi_x86_conv2d_NCHWc'
        # elif op_name == 'depthwise_conv2d_nchw':
        #     func_create = 'topi_x86_depthwise_conv2d_NCHWc_from_nchw'
        # else:
        #     func_create = tasks[i].name
        #     pass
        #     # raise ValueError("Tuning {} is not supported on x86".format(op_name))

        # task = autotvm.task.create(func_create, args=tsk.args,
        #                            target=target, template_key='direct')
        # task.workload = tsk.workload
        # tsk = task

        prefix = "[Task %2d/%2d] (%s)" %(i+1, len(tasks), tsk.name)

        # create tuner
        tuner = option['tuner']
        if tuner == 'xgb' or tuner == 'xgb-rank':
            tuner_obj = XGBTuner(tsk, loss_type='rank')
        elif tuner == 'ga':
            tuner_obj = GATuner(tsk, pop_size=100)
        elif tuner == 'random':
            tuner_obj = RandomTuner(tsk)
        elif tuner == 'gridsearch':
            tuner_obj = GridSearchTuner(tsk)
        else:
            raise ValueError("Invalid tuner: " + tuner)

        if option['use_transfer_learning']:
            if os.path.isfile(tmp_log_file):
                tuner_obj.load_history(autotvm.record.load_from_file(tmp_log_file))

        # do tuning
        n_trial = min(option['n_trial'], len(tsk.config_space))
        tuner_obj.tune(n_trial=n_trial,
                       early_stopping=option['early_stopping'],
                       measure_option=option['measure_option'],
                       callbacks=[
                           autotvm.callback.progress_bar(n_trial, prefix=prefix),
                           autotvm.callback.log_to_file(tmp_log_file)])

    if os.path.exists(option['log_best_file']):
        os.remove(option['log_best_file'])
    autotvm.record.pick_best(option['log_file'], option['log_best_file'])

# Use graph tuner to achieve graph level optimal schedules
# Set use_DP=False if it takes too long to finish.
def tune_graph(graph, dshape, records, opt_sch_file, use_DP=True):
    target_op = [relay.nn.conv2d]
    Tuner = DPTuner if use_DP else PBQPTuner
    executor = Tuner(graph, {input_name: dshape}, records, target_op, target)
    executor.benchmark_layout_transform(min_exec_num=2000)
    executor.run()
    executor.write_opt_sch2record_file(opt_sch_file)

```

tune 

```python
target = 'llvm' # 'cuda'
dtype = 'float32'
log_file = 'tune.log'
log_best_file = 'tune_best.log'
graph_opt_sch_file = 'graph_best.log'
path_lib = 'lib.so' #.o, .tar
path_graph = 'graph.json'
path_params = 'params.bin'
input_name = 'input_1'
data_shape = (1,3,224,224)
out_shape = (1, 1000)
ctx = tvm.context(str(target), 0) # tvm.cpu(),  tvm.gpu()
option = {
    'target': target,
    'log_file': log_file,
    'log_best_file': log_best_file,
    'graph_best_file': graph_opt_sch_file,
    'tuner': 'xgb', # random, ga, gridsearch, xgb
    'n_trial': 100,
    'early_stopping': 600,
    'try_winograd': False,
    'use_transfer_learning': False,
    'measure_option': autotvm.measure_option(
        builder=autotvm.LocalBuilder(timeout=10),
        runner=autotvm.LocalRunner(number=4, repeat=3, timeout=4, min_repeat_ms=150),
        # runner=autotvm.RPCRunner(
        #     '1080ti',  # change the device key to your key
        #     '0.0.0.0', 9190,
        #     number=20, repeat=3, timeout=4, min_repeat_ms=150)
    ),
}

mod, params_ = relay.frontend.from_xxx(xxx_model, shape={input_name: data_shape})

tasks = autotvm.task.extract_from_program(mod["main"], target=target,
                      params=params_, ops=(relay.op.nn.conv2d, relay.op.nn.dense))

# tune kernels
tune_tasks(option)
# tune graph
tune_graph(mod["main"], data_shape, option['log_file'], option['graph_best_file'])

# compile 
with autotvm.apply_history_best(opt_log_file): #autotvm.apply_graph_best(graph_opt_sch_file)
    with relay.build_config(opt_level=3):
        graph, lib, params = relay.build_module.build(mod, 
                                                      target=target, 
                                                      params=params_)
		# executor = relay.build_module.create_executor('graph', mod, ctx, target)

# run by executor
# out = executor.evaluate()(tvm.nd.array(x), **params_)        
        
# create runtime module
module = runtime.create(graph, lib, ctx)
module.set_input(**params)
module.set_input(input_name, data)
module.run()
out = module.get_output(0)

# save lib
lib.export_library(path_lib)
with open(path_graph, "w") as fo:
    fo.write(graph)
with open(path_params, "wb") as fo:
    fo.write(relay.save_param_dict(params))
        
# loading lib from files
loaded_lib = tvm.module.load(path_lib)
loaded_graph = open(path_graph).read()
loaded_params = bytearray(open(path_params, 'rb').read())

# create runtime module
## method 1
fcreate = tvm.get_global_func("tvm.graph_runtime.create")
gmodule = fcreate(loaded_graph, loaded_lib, ctx.device_type, ctx.device_id)
gmodule["load_params"](loaded_params)
gmodule["set_input"](input_name, data_tvm)
gmodule["run"]()
out = gmodule["get_output"](0)

## method 2
m = tvm.contrib.graph_runtime.create(loaded_graph, loaded_lib, ctx)
m.load_params(loaded_params)
m.run(**{input_name:data_tvm}) #or m.set_input(input_name, data_tvm); m.run()
out = m.get_output(0)
```

### C++ 调用 TVM lib

Makefile

```makefile
TVM_ROOT=path/to/tvm
# NNVM_PATH=nnvm
DMLC_CORE=${TVM_ROOT}/3rdparty/dmlc-core

PKG_CFLAGS = -std=c++11 -O2 -fPIC\
	-I${TVM_ROOT}/include\
	-I${DMLC_CORE}/include\
	-I${TVM_ROOT}/3rdparty/dlpack/include\
	-I/usr/local/cuda/include 

PKG_LDFLAGS = -ldl -lpthread -L/usr/local/cuda/lib64 -lcudart -lcuda

all: bin/demo

lib/libtvm_runtime_pack.o: tvm_runtime_pack.cc
	@mkdir -p $(@D)
	$(CXX) -c $(PKG_CFLAGS) -o $@  $^ 
	
lib/demo.o: demo.cc
	$(CXX) -c $(PKG_CFLAGS) -o $@  $^	
	
bin/demo: lib/demo.o lib/libtvm_runtime_pack.o
	@mkdir -p $(@D)
	$(CXX) $(PKG_CFLAGS) $(PKG_LDFLAGS) -o $@  $^	
```

tvm_runtime_pack.cc

```c++
/* 
see tvm/apps/howto_deploy/tvm_runtime_pack.cc
*/
#include "path/to/tvm/src/runtime/c_runtime_api.cc"
#include "path/to/tvm/src/runtime/cpu_device_api.cc"
#include "path/to/tvm/src/runtime/workspace_pool.cc"
#include "path/to/tvm/src/runtime/module_util.cc"
#include "path/to/tvm/src/runtime/module.cc"
#include "path/to/tvm/src/runtime/registry.cc"
#include "path/to/tvm/src/runtime/file_util.cc"
#include "path/to/tvm/src/runtime/threading_backend.cc"
#include "path/to/tvm/src/runtime/thread_pool.cc"
#include "path/to/tvm/src/runtime/ndarray.cc"

// Likely we only need to enable one of the following
// If you use Module::Load, use dso_module
// For system packed library, use system_lib_module
#include "path/to/tvm/src/runtime/dso_module.cc"
#include "path/to/tvm/src/runtime/system_lib_module.cc"

// Graph runtime
#include "path/to/tvm/src/runtime/graph/graph_runtime.cc"

#define TVM_CUDA_RUNTIME 1
#include "path/to/tvm/src/runtime/cuda/cuda_device_api.cc"
#include "path/to/tvm/src/runtime/cuda/cuda_module.cc"
```

demo.cc

```c++
#include <dlpack/dlpack.h>
#include <tvm/runtime/module.h>
#include <tvm/runtime/registry.h>
#include <tvm/runtime/packed_func.h>
#include <cuda.h>
#include <algorithm>
#include <fstream>
#include <iterator>
#include <stdexcept>
#include <string>
#include <ctime>
#include <cstdlib>

#define DEVICE_TYPE kDLGPU // or kDLCPU

void test()
{
    std::string lib_path, graph_path, params_path;
    lib_path = "lib.so";
    graph_path = "graph.json";
    params_path = "params.bin";
	std::string input_name = "input_1";
    
    // tvm module for compiled functions
    tvm::runtime::Module mod_syslib = tvm::runtime::Module::LoadFromFile(lib_path);
    // json graph
    std::ifstream json_in(graph_path, std::ios::in);
    std::string json_data((std::istreambuf_iterator<char>(json_in)), std::istreambuf_iterator<char>());
    json_in.close();
    // parameters in binary
    std::ifstream params_in(params_path, std::ios::binary);
    std::string params_data((std::istreambuf_iterator<char>(params_in)), std::istreambuf_iterator<char>());
    params_in.close();
    // parameters need to be TVMByteArray type to indicate the binary data
    TVMByteArray params_arr;
    params_arr.data = params_data.c_str();
    params_arr.size = params_data.length();

    int dtype_code = kDLFloat;
    int dtype_bits = 32;
    int dtype_lanes = 1;
    int device_id = 0;

    // get global function module for graph runtime
    tvm::runtime::Module mod = (*tvm::runtime::Registry::Get("tvm.graph_runtime.create"))(json_data, mod_syslib, (int)DEVICE_TYPE, device_id);

    int device_type = kDLCPU;
    DLTensor* x;
    int in_ndim = 4;
    int64_t in_shape[4] = {1, 3, 224, 224};
    TVMArrayAlloc(in_shape, in_ndim, dtype_code, dtype_bits, dtype_lanes, device_type, device_id, &x);

    // load image data saved in binary
    // const std::string data_filename = "cat.bin";
    // std::ifstream data_fin(data_filename, std::ios::binary);
    // if(!data_fin) throw std::runtime_error("Could not open: " + data_filename);
    // data_fin.read(static_cast<char*>(x->data), 3 * 224 * 224 * 4);
    std::srand(std::time(nullptr)); 
    for (auto i=0; i<1*3*224*224; i++) {
        static_cast<float*>(x->data)[i] = (float) std::rand()/RAND_MAX; 
    }
    x->strides = nullptr;
    x->byte_offset = 0;

    // get the function from the module(set input data)
    tvm::runtime::PackedFunc set_input = mod.GetFunction("set_input");
    // get the function from the module(load patameters)
    tvm::runtime::PackedFunc load_params = mod.GetFunction("load_params");
    load_params(params_arr);
    // get the function from the module(run it)
    tvm::runtime::PackedFunc run = mod.GetFunction("run");
    
    set_input(input_name, x);
    run();

    DLTensor* y;
    int out_ndim = 2;
    int64_t out_shape[2] = {1, 1000, };
    TVMArrayAlloc(out_shape, out_ndim, dtype_code, dtype_bits, dtype_lanes, device_type, device_id, &y);

    // get the function from the module(get output data)
    tvm::runtime::PackedFunc get_output = mod.GetFunction("get_output");
    get_output(0, y);

    // get the maximum position in output vector
    auto y_iter = static_cast<float*>(y->data);
    auto max_iter = std::max_element(y_iter, y_iter + 1000);
    auto max_index = std::distance(y_iter, max_iter);
    std::cout << "The maximum position in output vector is: " << max_index << std::endl;

    TVMArrayFree(x);
    TVMArrayFree(y);
}


int main(int argc, char **argv) {
    if (DEVICE_TYPE==kDLCPU) {
        std::cout << "Device type: CPU" << std::endl;
    } else {
        std::cout << "Device type: GPU" << std::endl;
    }
    test();
    return 0;
}

```

