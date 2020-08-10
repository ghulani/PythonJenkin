pipeline {
  agent any
  stages {
	stage('SCM Checkout'){
	git branch: 'master', 
	credentialsId: 'github', 
	url: 'https://github.com/ghulani/PythonJenkin'
   
   }
   stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
  }
}