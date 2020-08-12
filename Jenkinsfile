pipeline {
  agent any
  tools{
	
		maven "Maven3"
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
				rtMavenDeployer(
					id: "deployer",
					serverId: "nexus@123",
					releaseRepo: "pypi_host_nagp",
					snapshotRepo: "pypi_host_nagp"
				)
				rtMavenRun(
					pom: 'pom.xml',
					goals: 'clean install',
					deployerId: 'deployer',
					
				)
				rtPublishBuildInfo(
					serverId: "nexus@123"
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
