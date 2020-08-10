pipeline {
  agent any
  stages {
	stage('SCM Checkout'){
		steps{
			git branch: 'master', 
			credentialsId: 'github', 
			url: 'https://github.com/ghulani/PythonJenkin'
			}
		}
   stage('build') {
		steps {
        bat 'pip install -r requirements.txt'
      }
    }
  }
}
