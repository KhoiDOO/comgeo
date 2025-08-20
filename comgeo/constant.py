# Multi-processing constants
import multiprocessing


MAX_WORKERS = multiprocessing.cpu_count()
EIGHTY_WORKERS = round(MAX_WORKERS * 0.8)