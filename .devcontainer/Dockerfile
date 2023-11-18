
# Choose your desired base image
FROM jupyter/pyspark-notebook:latest

# name your environment and choose the python version
ARG conda_env=vscode_pyspark
ARG py_ver=3.11

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba create --yes -p "${CONDA_DIR}/envs/${conda_env}" python=${py_ver} ipython ipykernel && \ 
    mamba clean --all -f -y

# create Python kernel and link it to jupyter
RUN "${CONDA_DIR}/envs/${conda_env}/bin/python" -m ipykernel install --user --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# any additional pip installs can be added by uncommenting the following line
RUN "${CONDA_DIR}/envs/${conda_env}/bin/pip" install pyspark pandas --no-cache-dir && \ 
    "${CONDA_DIR}/envs/${conda_env}/bin/pip" install reverse_geocode && \ 
    "${CONDA_DIR}/envs/${conda_env}/bin/pip" install requests &&\
    "${CONDA_DIR}/envs/${conda_env}/bin/pip" install matplotlib &&\
    "${CONDA_DIR}/envs/${conda_env}/bin/pip" install seaborn &&\
    "${CONDA_DIR}/envs/${conda_env}/bin/pip" install basemap

# if you want this environment to be the default one, uncomment the following line:
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"
