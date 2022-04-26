import re

from os.path import join
from xmap.utils.assist import load_parameter
from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage


def submit_job(project_id, region, cluster_name):
    # this function requires google cloud project and also need to enable auth locally to pass identity verification.

    path_local = "./"
    path_para = join(path_local, "parameters.yaml")
    print(path_para)
    para = load_parameter(path_para)

    job_class = para['init']['class']
    extra_files = para['init']['files_egg']
    extra_dat_files = para['init']['files']
    job_client = dataproc.JobControllerClient(
        client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(region)}
    )

    
    job = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {
            "main_python_file_uri": job_class,
            "python_file_uris": [extra_files],
            "file_uris": [extra_dat_files],
        },
    }

    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job}
    )
    response = operation.result()

    matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)

    output = (
        storage.Client()
        .get_bucket(matches.group(1))
        .blob(f"{matches.group(2)}.000000000")
        .download_as_string()
    )

    print(f"Job finished successfully: {output}")