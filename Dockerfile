
FROM jupyter/base-notebook:latest


WORKDIR /app


COPY notebook.ipynb /app/notebook.ipynb


EXPOSE 8888


CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]