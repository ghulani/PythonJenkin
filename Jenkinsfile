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
	
		environment {
			NEXUS_VERSION = "nexus3"
			NEXUS_PROTOCOL = "http"
			NEXUS_URL = "http://127.0.0.1:8081"
			NEXUS_REPOSITORY = "pypi_host_nagp"
			NEXUS_CREDENTIAL_ID = "nexus-cred"
		}
	
		steps {
                script {
                    pom = readMavenPom file: "pom.xml";
                    filesByGlob = findFiles(glob: "target/*.${pom.packaging}");
                    echo "${filesByGlob[0].name} ${filesByGlob[0].path} ${filesByGlob[0].directory} ${filesByGlob[0].length} ${filesByGlob[0].lastModified}"
                    artifactPath = filesByGlob[0].path;
                    artifactExists = fileExists artifactPath;
                    if(artifactExists) {
                        echo "*** File: ${artifactPath}, group: ${pom.groupId}, packaging: ${pom.packaging}, version ${pom.version}";
						nexusArtifactUploader(
						artifacts: [[artifactId: 'nexus@123', classifier: '', file: 'target/pipline_nagp-0.0.1-SNAPSHOT.war', type: 'war']],
						credentialsId: 'e9e0853f-14c6-4e1a-875a-1421c54749fb',
						groupId: 'com.easy', nexusUrl: 'http://127.0.0.1:8081',
						nexusVersion: 'nexus3', 
						protocol: 'http', 
						repository: 'http://127.0.0.1:8081/repository/pypi_host_nagp/', 
						version: '0.0.1-SNAPSHOT'
						);
                        
                    } else {
                        error "*** File: ${artifactPath}, could not be found";
                    }
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
