pipeline {
  agent any
  //tools{
	//	maven "Maven3"
  //}
  
  
  options {
		skipDefaultCheckout()
  
  }
  environment {

				dockerbuild = ''
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
				spec: '''{"files":[{"pattern":"/src/","target":"result/src","recursive": "false"}]}'''
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
  
	stage("Create Docker Image"){
		environment {
				dockerHome = tool 'docker'
			}
		steps{
			bat ' cd /D %dockerHome% && call docker build -t ghulani/pythondemo --no-cache -f Dockerfile .'
			//script{
			//	dockerbuild = docker.build("ghulani/pythondemo")
			//}
		}
	}
	stage("Push to Docker Hub"){
			
		steps{
			
			withCredentials([[$class: 'UsernamePasswordMultiBinding',credentialsId: 'docker-hub', passwordVariable: 'pass']]) {
			//withCredentials([usernamePassword(credentialsId: 'DP', passwordVariable: 'pass')]) {
				// the code in here can access $pass and $user
				//bat 'DockerHubP | docker login --username ghulani --password-stdin'
				
					echo '%pass%'
					echo '$pass'
				
				bat 'docker login -u=ghulani -p=%pass%'
				bat 'docker push ghulani/pythondemo'
			}
	
			//script{
			
			//	docker.withRegistry( 'https://hub.docker.com/', 'docker-hub' ) {
			//	dockerbuild.push()
			//	}
			//}
			//bat 'DockerHubP | docker login --username ghulani --password-stdin'
			//bat 'docker push ghulani/pythondemo '
		}
	
	}
	stage("Stoping running container"){
		steps{
			bat 'netstat -ano | findStr "800"'
			//sh '''
			//ContainerID = $(docker ps | grep 800 | cut -d " " -f 1)
			//if [$ContainerID]
			//then
			//	docker stop $ContainerID
			//	docker rm -f $ContainerID
			//fi
			//'''
		}
	}
	stage("Docker Deployment"){
		steps{
			bat 'docker run --name pythondemo -d -p 800:8080 ghulani/pythondemo'
		}
	}
  
  
	//post {
	//      always {
	//         junit 'build/reports/**/*.xml'
	//     }
	// }
	}
}
