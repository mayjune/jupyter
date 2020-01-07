if __name__ == "__main__":
    dockerfile = '''
FROM continuumio/anaconda3
RUN pip install --upgrade pip
'''
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile += "RUN pip install {}\n".format(l)

    dockerfile += '''
RUN jupyter contrib nbextension install --user
WORKDIR /jupyter
'''
    with open('Dockerfile', 'w') as file :
        file.write(dockerfile)
