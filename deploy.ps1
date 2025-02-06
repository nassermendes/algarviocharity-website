param(
    [Parameter(Mandatory=$true)]
    [string]$message
)

Write-Host "🔄 Pulling latest changes..." -ForegroundColor Blue
git pull origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Pull failed. Please resolve conflicts and try again." -ForegroundColor Red
    exit 1
}

Write-Host "➕ Adding changes..." -ForegroundColor Blue
git add .

Write-Host "💾 Committing changes..." -ForegroundColor Blue
git commit -m "$message"

Write-Host "⬆️ Pushing to GitHub..." -ForegroundColor Blue
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Successfully deployed! Changes will be live in a few minutes." -ForegroundColor Green
} else {
    Write-Host "❌ Push failed. Please check the error message above." -ForegroundColor Red
}
