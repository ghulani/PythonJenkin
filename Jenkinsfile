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
		steps{
			withSonarQubeEnv('SonarQube') {
			bat 'cd  /D %scannerHome%  && call bin/sonar-scanner.bat'
			}
		}
		
	}
	//stage('Upload to Artifactory'){	
	//	environment {
	//		NEXUS_VERSION = "nexus3"
	//		NEXUS_PROTOCOL = "http"
	//		NEXUS_URL = "http://127.0.0.1:8081"
	//		NEXUS_REPOSITORY = "pypi_host_nagp"
	//		NEXUS_CREDENTIAL_ID = "nexus-cred"
	//	}
	//	steps{
		
	//	}

	//}
	

  
	//post {
	//      always {
	//         junit 'build/reports/**/*.xml'
	//     }
	// }
	}
}
