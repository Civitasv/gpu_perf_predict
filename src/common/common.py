#!/usr/bin/python3

import csv
import re
import os
import statistics
import subprocess


def run_traces(programs, parameters):
    subprocess.check_output("rm -f *.csv",  shell = True)
    traces = [" ", "--metrics all", "--events all"]
    for trace in traces:
        for program in programs:
            for param in parameters:
                cmd = "nvprof"
                cmd += " --normalized-time-unit " + "s"
                cmd += " --print-gpu-trace "
                if trace == " ":
                    cmd += trace
                elif trace == "--metrics all":
                    cmd += trace
                elif trace == "--events all":
                    cmd += trace

                cmd += " --csv " 
                cmd += " ./"
                cmd += program
                cmd += " " + param  
                if trace == " ":
                    cmd += " 2> Temp; cat Temp | tail -n4 >>  ./traces.csv"
                elif trace == "--metrics all":
                    cmd += " 2> Temp; cat Temp | grep 'Tesla' >> ./metrics.csv"
                elif trace == "--events all":
                    cmd += " 2> Temp; cat Temp | grep 'Tesla' >> ./events.csv"

                output = subprocess.check_output(cmd,  shell = True)#, stderr=subprocess.STDOUT)
                #print("Primeiro{}".format(output))


#TODO Grep Tesla K40 y PArametros fijos


