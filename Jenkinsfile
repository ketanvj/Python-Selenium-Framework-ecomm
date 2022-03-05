pipeline{
    agent any
    stages {
        stage('Create Virtual Env') {
            steps {bat '''python -m venv env
                call .\\env\\scripts\\activate
                pip install -r requirements.txt
                cmdline.bat'''
                }
            }
        }
    }