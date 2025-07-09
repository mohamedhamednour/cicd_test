pipeline {
    agent any

    environment {
        POSTGRES_DB = 'cicd'
        POSTGRES_USER = 'postgres'
        POSTGRES_PASSWORD = 'password'
        POSTGRES_HOST = 'localhost'
        POSTGRES_PORT = '5432'
        DJANGO_SETTINGS_MODULE = 'shopping.settings'
        PYTHONPATH = './'
    }

    stages {
        stage('Start PostgreSQL') {
            steps {
                script {
                    echo "🛢️ Starting PostgreSQL container..."
                    docker.image('postgres:14').withRun(
                        "-e POSTGRES_USER=${env.POSTGRES_USER} " +
                        "-e POSTGRES_PASSWORD=${env.POSTGRES_PASSWORD} " +
                        "-e POSTGRES_DB=${env.POSTGRES_DB} " +
                        "-p ${env.POSTGRES_PORT}:5432"
                    ) { postgresContainer ->
                        echo "⏳ Waiting for PostgreSQL to be ready..."
                        sleep(time: 10, unit: 'SECONDS')
                    }
                }
            }
        }

        stage('Checkout Code') {
            steps {
                echo "📦 Checking out source code..."
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo "🐍 Setting up Python & virtualenv..."
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations & Tests') {
            steps {
                echo "🧪 Running Django migrations & tests..."
                sh '''
                    source venv/bin/activate
                    python manage.py migrate
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo "🧪 Running tests..."
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy 🚀') {
            when {
                branch 'main'
            }
            steps {
                echo "🚀 Deployment step running... (this is just a test CD step)"
            }
        }
    }

    post {
        always {
            echo "📋 Pipeline finished. Cleaning up if needed."
        }
    }
}
