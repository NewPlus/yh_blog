npm run build
aws s3 sync ./build s3://yonghwan.kr --profile=default --exclude '.env' --exclude 'node_modules/*' --exclude 'prd/*'
