pipeline{
    stage('Create Virtual Env') {
        bat '''python -m venv env
        call .\\env\\scripts\\activate
        pip install -r requirements.txt
        cmdline.bat'''
        }
    }
}