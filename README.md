# Tourist Safety Dashboard

A comprehensive tourist safety dashboard with real-time monitoring capabilities, built with Next.js 14+ and FastAPI.

## Features

### Core Features (Phase 1)
- **Interactive Map Component**: World map using Leaflet with tourist location markers
- **Tourist Lookup**: Search and filter tourists by name, email, or ID
- **Alerts Feed**: Real-time alerts with different severity levels
- **Dashboard Overview**: Statistics cards showing key metrics
- **Responsive Design**: Mobile-first approach with clean, modern UI

### Tech Stack
- **Frontend**: Next.js 14+ with TypeScript
- **Backend**: FastAPI (Python)
- **Styling**: Tailwind CSS
- **Database**: SQLite
- **Map Library**: Leaflet with React-Leaflet

## Getting Started

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tourist-safety-dashboard
   ```

2. **Install root dependencies**
   ```bash
   npm install
   ```

3. **Set up the backend**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python seed_data.py  # Populate database with sample data
   ```

4. **Set up the frontend**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

**Option 1: Run both frontend and backend together**
```bash
# From the root directory
npm run dev
```

**Option 2: Run separately**

Backend (Terminal 1):
```bash
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Frontend (Terminal 2):
```bash
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## API Endpoints

### Tourists
- `GET /api/tourists` - Get all tourists
- `GET /api/tourists/{id}` - Get specific tourist
- `POST /api/tourists` - Create new tourist

### Alerts
- `GET /api/alerts` - Get recent alerts
- `POST /api/alerts` - Create new alert

### Statistics
- `GET /api/stats` - Get dashboard statistics

## Project Structure

```
tourist-safety-dashboard/
├── frontend/                 # Next.js frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── Map/        # Map-related components
│   │   │   ├── Dashboard/  # Dashboard components
│   │   │   ├── Alerts/    # Alert components
│   │   │   └── Search/    # Search components
│   │   ├── utils/         # Utility functions
│   │   └── app/          # Next.js app directory
│   └── package.json
├── backend/                # FastAPI backend
│   ├── models/            # Database models
│   ├── routes/            # API routes
│   ├── database/          # Database configuration
│   ├── main.py           # FastAPI application
│   └── requirements.txt
└── package.json          # Root package.json
```

## Sample Data

The application comes with pre-populated sample data including:
- 15 sample tourists with coordinates from popular tourist destinations
- 20 sample alerts with different types and severity levels
- Basic statistics for dashboard overview

## Features Overview

### Interactive Map
- Displays tourists as colored markers based on status
- Click markers to view tourist details
- Search functionality to locate specific tourists
- Responsive design that works on all devices

### Tourist Management
- Search by name, email, or ID
- View detailed tourist information
- Real-time status updates
- Location history tracking

### Alerts System
- Real-time alert feed
- Different alert types: location updates, risk zone entries, check-ins
- Severity levels: low, medium, high, critical
- Alert resolution tracking

### Dashboard Statistics
- Total tourists count
- Active tourists count
- Unresolved alerts count
- Risk zones count

## Development

### Adding New Features
1. Backend: Add new models in `backend/models/`, routes in `backend/routes/`
2. Frontend: Add new components in `frontend/src/components/`
3. Update API client in `frontend/src/utils/api.ts`

### Database Changes
- Modify models in `backend/models/`
- Run `python seed_data.py` to reset and populate database

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
