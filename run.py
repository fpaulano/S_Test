import logging
import sys

import cytomine

from cytomine.models import Job


__version__ = "0.0.1"


def run(cyto_job, parameters):
    logging.info("----- IA results uploader v%s -----", __version__)

    job = cyto_job.job

    job.update(progress=0, status=Job.RUNNING, statusComment=f"Starting test")


    job.update(progress=100, status=Job.TERMINATED, statusComment="Test finished")


if __name__ == "__main__":
    logging.debug("Command: %s", sys.argv)

    with cytomine.CytomineJob.from_cli(sys.argv) as cyto_job:
        run(cyto_job, cyto_job.parameters)
