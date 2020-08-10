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
		def cmd_exec(command) {
			return bat(returnStdout: true, script: "${command}sonar-scanner.bat").trim()
		}
		steps{
			withSonarQubeEnv('SonarQube') {
			cmd_exec ('echo %scannerHome%)	'
			}
		}
		
	}
  
	//post {
	//      always {
	//         junit 'build/reports/**/*.xml'
	//     }
	// }
	}
}