#!/usr/bin/python3

import imp
common = imp.load_source("common", "../common/common.py")

result_file = "matmul.csv"
programs = ["matmul_gpu", "matmul_gpu_uncoalesced",
            "matMul_gpu_sharedmem_uncoalesced", "matMul_gpu_sharedmem"]
device_id = 0

matrix_sizes = ["256 16 0"]# 512, 1024, 2048, 4096, 8192]

common.run_traces(result_file, programs, matrix_sizes, device_id)
