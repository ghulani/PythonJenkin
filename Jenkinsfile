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
	stage('Unit tests'){
		steps{
			bat 'pytest --junitxml test-results.xml "src/tests/test1.py"'
		}
	}
	
	stage('SonarQube') {
		environment {
			scannerHome = tool 'SonarScanner'
		}
		withSonarQubeEnv('SonarQube') {
            bat '${scannerHome}sonar-scanner.bat'
        }
	}
  
	//post {
	//      always {
	//         junit 'build/reports/**/*.xml'
	//     }
	// }
	}
}