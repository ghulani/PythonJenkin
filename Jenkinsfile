pipeline {
  agent any
  //tools{
	//	maven "Maven3"
  //}
  options {
		skipDefaultCheckout()
  
  }
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
	stage('Upload to Artifactory'){
	
		steps{
			rtUpload(
				buildName: "pipeline_nagp",
				buildNumber: "1.0.0",
				serverId: "artifactory",
				spec: '''{"files":[{"pattern":"/src/","target":"result/","recursive": "false"}]}'''
			)
		}
	}	
	stage("Publish build info"){
		steps{
			rtPublishBuildInfo(
				buildName:"pipeline_nagp",
				buildNumber: "1.0.0",
				serverId: "artifactory"
			)
		}
	}
  
	//post {
	//      always {
	//         junit 'build/reports/**/*.xml'
	//     }
	// }
	}
}
