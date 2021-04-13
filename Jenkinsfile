pipeline{
    agent any
    stages{
        stage("Git Checkout"){
            steps{
                git branch: 'main', url: 'https://github.com/rajagspann/assignment'
            }
        }
        stage("Executing script to get the SSL Cert details"){
            steps{
                sh "./ssl_expr_check.py > sorted_ssl_details"
            }
        }
        stage("Open the ssl file"){
            steps{
                sh "cat sorted_ssl_details"
            }
        }
        stage("Update Git repo"){
            steps{
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                        withCredentials([usernamePassword(credentialsId: 'gitcreds', passwordVariable: 'GIT_PWD', usernameVariable: 'GIT_UNAME')]){
                            def encodedPassword = URLEncoder.encode("$GIT_PWD",'UTF-8')
                            sh "git config user.email rajak.dop@gmail.com"
                            sh "git config user.name rajagspann"
                            sh "git add sorted_ssl_details"
                            sh "git commit -m 'Updating Git'"
                            sh "git push https://${GIT_UNAME}:${encodedPassword}@github.com/${GIT_UNAME}/assignment.git"
                        }
                    }
                }
            }
        }
    }
}

