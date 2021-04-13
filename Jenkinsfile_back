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
    }
}
