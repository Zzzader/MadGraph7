import gitlab
import os
from dotenv import load_dotenv

import sys


load_dotenv()

# needed:
#dev
gl = gitlab.Gitlab(url="https://gitlab.cern.ch", private_token=os.getenv("GITLAB_API_KEY"))

project = gl.projects.get(os.getenv("PROJECT_ID"))
pipeline = project.pipelines.get(sys.argv[1])

def main():
    # job_list = get_job_of_pipeline()
    # log_list = retrieve_job_logs(job_list)
    # save_job_logs(log_list)
    # show_job_logs_on_console(log_list)

    show_job_logs_on_console()

# def get_job_of_pipeline():
#     jobs = pipeline.jobs.list(get_all=True)
#     job_list = []
#
#     for j in jobs:
#         job = project.jobs.get(j.id)
#         job_list.append(job)
#
#     return job_list
#
# ## create dictionary with id's and logfiles
# def retrieve_job_logs(job_list):
#
#     log_dict_list = []
#     for job in job_list:
#         log_file = job.trace()
#         log_dict = {'id': job.id, 'log_file': log_file}
#         log_dict_list.append(log_dict)
#
#     return log_dict_list

#saving in files on runner? or simply printing the outputs to terminal? -> which works and does not require a new job
# def save_job_logs(log_list):
#     if not os.path.exists("./logs"):
#         os.mkdir("logs")
#     else:
#         print("directory already exists!")
#     for log in log_list:
#         if not os.path.exists(f"./logs/Log_of_file {log["id"]}.txt"):
#             new_file = f"./logs/Log_of_file {log["id"]}.txt"
#             with open(new_file, "w", encoding='utf-8') as f:
#                 f.write(str(log["log_file"]))
#                 print(f"writing file with id: {log["id"]}")
#                 print(str(log["log_file"]))
#
#         else:
#             print("Log file already exists")

def show_job_logs_on_console():
    # for log in log_list:
    #     print(f"Log of job ID: {log["id"]}")
    #     print(str(log["log_file"]))
    raise Exception("Testing failing job")


if __name__ == "__main__":
    main()