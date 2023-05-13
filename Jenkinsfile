pipeline {
    agent any

    environment {
        registry = "dhanush29/wescribe-backend"
        registryCredential = "docker_credentials"
        dockerImage = ""
    }

    stages {

        stage('Pull GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/We-Scribe/WeScribe-Backend'
            }
        }

        // stage('Setup Python Virtual Environment'){
        //     steps {
        //         sh '''
        //             pipenv shell
        //             pipenv install -r requirements.txt
        //             exit
        //             '''
        //     }
        // }

        // stage('Run Django Tests'){
        //     steps {
        //         sh '''
        //             pipenv shell
        //             python3 backend/manage.py test
        //             exit
        //             '''
        //     }
        // }

        stage('Docker Image Build') {
            steps {
                    script {
                        dockerImage = docker.build(registry + ":latest")
                    }
                }
        }

        stage('DockerHub Image Push') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Ansible Deployment') {
            steps {
                ansiblePlaybook colorized: true,
                installation: 'Ansible',
                inventory: 'inventory',
                playbook: 'playbook.yml'
            }
        }
    }
}