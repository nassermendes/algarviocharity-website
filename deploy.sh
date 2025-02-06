#!/bin/bash

# Check if a commit message was provided
if [ $# -eq 0 ]; then
    echo "❌ Error: Please provide a commit message"
    echo "Usage: ./deploy.sh \"Your commit message\""
    exit 1
fi

# Store the commit message
message="$1"

# Colors for output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔄 Pulling latest changes...${NC}"
git pull origin main

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Pull failed. Please resolve conflicts and try again.${NC}"
    exit 1
fi

echo -e "${BLUE}➕ Adding changes...${NC}"
git add .

echo -e "${BLUE}💾 Committing changes...${NC}"
git commit -m "$message"

echo -e "${BLUE}⬆️ Pushing to GitHub...${NC}"
git push origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Successfully deployed! Changes will be live in a few minutes.${NC}"
else
    echo -e "${RED}❌ Push failed. Please check the error message above.${NC}"
fi
