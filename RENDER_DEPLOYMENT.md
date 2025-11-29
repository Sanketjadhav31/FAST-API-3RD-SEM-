# 🚀 Complete Render Deployment Guide

## Step-by-Step Guide to Deploy Task Management API on Render

---

## 📋 Prerequisites

1. ✅ GitHub account with your repository
2. ✅ Render account (free tier available at https://render.com)
3. ✅ Your code pushed to GitHub (already done ✓)

---

## 🔧 Step 1: Prepare Your Project for Render

### 1.1 Verify Required Files

Your project already has these files (✓):
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration
- `.env.example` - Environment variables template

---

## 🌐 Step 2: Create Render Account

1. Go to https://render.com
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with:
   - GitHub account (recommended) - allows easy repo connection
   - Or email/password
4. Verify your email if required

---

## 🔗 Step 3: Connect GitHub Repository

1. Log in to Render Dashboard: https://dashboard.render.com
2. Click **"New +"** button (top right)
3. Select **"Web Service"**
4. You'll see two options:
   - **Connect GitHub** (if not already connected)
   - **Use existing repository**

### If GitHub not connected:
1. Click **"Connect GitHub"**
2. Authorize Render to access your GitHub
3. Select repositories to grant access:
   - Choose **"Only select repositories"**
   - Select: `FAST-API-3RD-SEM-`
   - Click **"Install & Authorize"**

### If GitHub already connected:
1. Search for your repository: `FAST-API-3RD-SEM-`
2. Click **"Connect"**

---

## ⚙️ Step 4: Configure Web Service

### 4.1 Basic Settings

Fill in the following fields:

**Name**: `task-management-api` (or your preferred name)
- This will be part of your URL: `task-management-api.onrender.com`

**Region**: Choose closest to you
- `Oregon (US West)`
- `Ohio (US East)`
- `Frankfurt (EU Central)`
- `Singapore (Southeast Asia)`

**Branch**: `main`
- This is your production branch

**Root Directory**: Leave blank
- Your app is in the root directory

**Runtime**: `Python 3`
- Render will auto-detect this

### 4.2 Build & Start Commands

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

> **Important**: Use `$PORT` - Render assigns this dynamically

### 4.3 Instance Type

**Free Tier** (for testing):
- Select **"Free"**
- 512 MB RAM
- Shared CPU
- Spins down after 15 minutes of inactivity
- Spins up on first request (may take 30-60 seconds)

**Paid Tier** (for production):
- Select **"Starter"** ($7/month) or higher
- Always running
- Better performance

---

## 🔐 Step 5: Set Environment Variables

Scroll down to **"Environment Variables"** section:

Click **"Add Environment Variable"** and add:

### Required Variables:

1. **DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: sqlite:///./task_management.db
   ```

2. **ENVIRONMENT**
   ```
   Key: ENVIRONMENT
   Value: production
   ```

3. **LOG_LEVEL**
   ```
   Key: LOG_LEVEL
   Value: INFO
   ```

4. **ALLOWED_ORIGINS** (for CORS)
   ```
   Key: ALLOWED_ORIGINS
   Value: *
   ```
   > For production, replace `*` with your frontend domain

### Optional Variables:

5. **WORKERS**
   ```
   Key: WORKERS
   Value: 2
   ```

---

## 🎯 Step 6: Advanced Settings (Optional)

### Auto-Deploy
- ✅ **Enable** "Auto-Deploy"
- Your app will redeploy automatically when you push to `main` branch

### Health Check Path
- Set to: `/health`
- Render will ping this endpoint to check if your app is running

### Docker Configuration (Alternative)
If you prefer Docker deployment:
1. Change **"Build Command"** to: `docker build -t task-api .`
2. Change **"Start Command"** to: `docker run -p $PORT:8000 task-api`

---

## 🚀 Step 7: Deploy!

1. Review all settings
2. Click **"Create Web Service"** button at the bottom
3. Render will start building your application

### Deployment Process:
```
1. Cloning repository... ✓
2. Installing dependencies... ✓
3. Building application... ✓
4. Starting service... ✓
5. Health check... ✓
6. Live! 🎉
```

This usually takes **2-5 minutes** for first deployment.

---

## 📊 Step 8: Monitor Deployment

### View Logs:
1. Go to your service dashboard
2. Click **"Logs"** tab
3. Watch real-time deployment logs

### Expected Log Output:
```
==> Cloning from https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-...
==> Downloading cache...
==> Installing dependencies...
==> Building...
==> Starting service...
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
```

---

## 🗄️ Step 9: Setup Database (PostgreSQL - Recommended for Production)

### Why PostgreSQL?
- SQLite doesn't persist on Render's free tier
- PostgreSQL is free on Render
- Better for production

### Create PostgreSQL Database:

1. Go to Render Dashboard
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `task-management-db`
   - **Database**: `task_management`
   - **User**: (auto-generated)
   - **Region**: Same as your web service
   - **Instance Type**: **Free**
4. Click **"Create Database"**

### Connect Database to Web Service:

1. Go to your PostgreSQL database page
2. Copy **"Internal Database URL"**
3. Go back to your Web Service
4. Click **"Environment"** tab
5. Edit `DATABASE_URL` variable:
   - Paste the PostgreSQL URL
   - Example: `postgresql://user:pass@host/dbname`
6. Click **"Save Changes"**
7. Service will automatically redeploy

### Update requirements.txt for PostgreSQL:

Add to `requirements.txt`:
```
psycopg2-binary==2.9.9
```

Commit and push:
```bash
git add requirements.txt
git commit -m "feat: Add PostgreSQL support for Render deployment"
git push origin main
```

---

## 🌱 Step 10: Seed the Database

### Option 1: Using Render Shell

1. Go to your Web Service dashboard
2. Click **"Shell"** tab (top right)
3. Click **"Launch Shell"**
4. Run:
   ```bash
   python seed.py
   ```

### Option 2: Create a Seed Endpoint (Recommended)

Add to `app/main.py`:
```python
@app.post("/seed-database", tags=["Admin"])
def seed_database_endpoint(session: Session = Depends(get_session)):
    """Seed database with sample data (use once)"""
    # Add your seed logic here
    return {"message": "Database seeded successfully"}
```

Then visit: `https://your-app.onrender.com/seed-database`

---

## ✅ Step 11: Verify Deployment

### Check Your API:

1. **Root Endpoint**:
   ```
   https://task-management-api.onrender.com/
   ```
   Expected: Welcome message

2. **Health Check**:
   ```
   https://task-management-api.onrender.com/health
   ```
   Expected: `{"status": "healthy"}`

3. **API Documentation**:
   ```
   https://task-management-api.onrender.com/docs
   ```
   Expected: Swagger UI

4. **Test Endpoints**:
   ```bash
   # Get all tasks
   curl https://task-management-api.onrender.com/tasks
   
   # Create a task
   curl -X POST https://task-management-api.onrender.com/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"Test Task","status":"todo","priority":"high"}'
   ```

---

## 🔧 Step 12: Custom Domain (Optional)

### Add Your Own Domain:

1. Go to your Web Service dashboard
2. Click **"Settings"** tab
3. Scroll to **"Custom Domain"**
4. Click **"Add Custom Domain"**
5. Enter your domain: `api.yourdomain.com`
6. Add DNS records to your domain provider:
   ```
   Type: CNAME
   Name: api
   Value: task-management-api.onrender.com
   ```
7. Wait for DNS propagation (5-30 minutes)
8. Render will automatically provision SSL certificate

---

## 📈 Step 13: Monitor Your Application

### Render Dashboard Features:

1. **Metrics**:
   - CPU usage
   - Memory usage
   - Request count
   - Response times

2. **Logs**:
   - Real-time application logs
   - Error tracking
   - Request logs

3. **Events**:
   - Deployment history
   - Service restarts
   - Health check failures

### Set Up Alerts:

1. Go to **"Settings"** → **"Notifications"**
2. Add email for:
   - Deploy failures
   - Service crashes
   - Health check failures

---

## 🐛 Troubleshooting

### Issue 1: Build Failed

**Error**: `Could not find requirements.txt`

**Solution**:
```bash
# Ensure requirements.txt is in root directory
git add requirements.txt
git commit -m "fix: Add requirements.txt"
git push origin main
```

### Issue 2: Application Not Starting

**Error**: `Application failed to respond to health check`

**Solution**:
1. Check logs for errors
2. Verify start command uses `$PORT`:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

### Issue 3: Database Connection Failed

**Error**: `could not connect to database`

**Solution**:
1. Verify `DATABASE_URL` is set correctly
2. For PostgreSQL, ensure `psycopg2-binary` is in requirements.txt
3. Check database is running in Render dashboard

### Issue 4: CORS Errors

**Error**: `Access-Control-Allow-Origin`

**Solution**:
Update `app/main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend.com"],  # Update this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Issue 5: Free Tier Sleeping

**Issue**: App takes 30-60 seconds to respond

**Solution**:
- This is normal for free tier
- Upgrade to paid tier for always-on service
- Or use a service like UptimeRobot to ping your app every 5 minutes

---

## 💰 Pricing

### Free Tier:
- ✅ 750 hours/month (enough for 1 service)
- ✅ 512 MB RAM
- ✅ Shared CPU
- ⚠️ Spins down after 15 min inactivity
- ✅ Free PostgreSQL (90 days, then $7/month)

### Starter Tier ($7/month):
- ✅ Always running
- ✅ 512 MB RAM
- ✅ Shared CPU
- ✅ Better performance

### Standard Tier ($25/month):
- ✅ 2 GB RAM
- ✅ Dedicated CPU
- ✅ Auto-scaling
- ✅ Priority support

---

## 🔄 Continuous Deployment

### Automatic Deployments:

Every time you push to `main` branch:
```bash
git add .
git commit -m "feat: Add new feature"
git push origin main
```

Render will automatically:
1. Detect the push
2. Pull latest code
3. Run build command
4. Deploy new version
5. Run health checks
6. Switch traffic to new version

### Manual Deployments:

1. Go to your service dashboard
2. Click **"Manual Deploy"**
3. Select branch: `main`
4. Click **"Deploy"**

---

## 📊 Post-Deployment Checklist

- [ ] API is accessible at your Render URL
- [ ] Health check endpoint returns 200
- [ ] Swagger docs are accessible at `/docs`
- [ ] Database is connected and working
- [ ] Sample data seeded (if needed)
- [ ] All endpoints tested and working
- [ ] CORS configured for your frontend
- [ ] Environment variables set correctly
- [ ] Logs show no errors
- [ ] Custom domain configured (if applicable)
- [ ] Monitoring and alerts set up

---

## 🎉 Success!

Your Task Management API is now live on Render!

**Your API URLs**:
- Production: `https://task-management-api.onrender.com`
- Swagger Docs: `https://task-management-api.onrender.com/docs`
- Health Check: `https://task-management-api.onrender.com/health`

---

## 📚 Additional Resources

- **Render Docs**: https://render.com/docs
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Your Repository**: https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-

---

## 🆘 Need Help?

1. **Render Support**: https://render.com/docs/support
2. **Community Forum**: https://community.render.com
3. **GitHub Issues**: Open an issue in your repository

---

**Deployment Guide Created**: November 29, 2025  
**Maintained by**: Sanket Jadhav  
**Status**: ✅ Ready for Deployment
