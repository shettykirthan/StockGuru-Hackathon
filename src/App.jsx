
import { UploadCloud, BarChart2, MessageCircle,  Eye, GitBranch, } from 'lucide-react';
import './App.css'; 
import welcomeGIF from './assets/welcome.json';
import Lottie from 'lottie-react';

function App() {
  return (
    <div className="app-container">
      <main className="main-container">
       
       {/* Welcome Section */}
        <div className="welcome-section">
          <div className="welcome-left">
            <h1 className="sname" >StockGuru</h1>
            <h1 className="app-title">Invest Smarter,Faster</h1>
            <p className="app-description">
             Personalized AI-driven insights for smarter investments.
            </p>
            <a href="http://localhost:8501/" className="get-started-btn-link">
              <button className="get-started-btn">Get Started</button>
            </a>
          </div>
          <div className="welcome-right">
            <Lottie animationData={welcomeGIF} />
          </div>
        </div>
        {/* <h2 className="title1">About </h2>
<div className="container1">
  <div className="content">
   
    <div className="text-content">
      <p>
        Stocks Guru is your premier destination for comprehensive stock
        market analysis, insights, and financial news. Our mission is to
        empower investors with the knowledge and tools they need to make
        informed decisions in the ever-changing world of finance.
      </p>
      <p>
        Founded by a team of experienced financial analysts and technology
        experts, Stocks Guru combines cutting-edge data analysis with
        expert commentary to provide you with a clear picture of market
        trends and opportunities.
      </p>
      <p>
        Whether you're a seasoned investor or just starting your financial
        journey, Stocks Guru is here to guide you through the complexities
        of the stock market and help you achieve your investment goals.
      </p>
    </div>

   
    <div className="image-content">
      <img
        src="test.jpg" 
        alt="Stocks Guru"
        className="image"
      />
    </div>
  </div>
</div> */}
        {/* Features Section */}
        <h1 className='titles' style={{ textAlign: "center" }}>Features</h1>
        <div className="features-container">
          <div className="feature-item">
            <UploadCloud style={{ height: '3rem', width: '3rem', color: '#3B82F6' }} />
            <h2 className="feature-title">Markets</h2>
            <p className="feature-description">Explore real-time stock market data and trends to stay informed about the latest financial movements.</p>
          </div>
          <div className="feature-item">
            <BarChart2 style={{ height: '3rem', width: '3rem', color: '#22C55E' }} />
            <h2 className="feature-title">News</h2>
            <p className="feature-description">Access up-to-date financial news to keep track of events impacting the market</p>
          </div>
          <div className="feature-item">
            <MessageCircle style={{ height: '3rem', width: '3rem', color: '#A78BFA' }} />
            <h2 className="feature-title">Insights</h2>
            <p className="feature-description">Gain expert analysis and insights to better understand market opportunities and risks</p>
          </div>
          <div className="feature-item">
            <Eye style={{ height: '3rem', width: '3rem', color: '#EF4444' }} />
            <h2 className="feature-title">Reports</h2>
            <p className="feature-description">Access comprehensive reports to make informed investment decisions based on in-depth analyses</p>
          </div>
          <div className="feature-item">
            <GitBranch style={{ height: '3rem', width: '3rem', color: '#10B981' }} />
            <h2 className="feature-title">My Profile</h2>
            <p className="feature-description">Manage and personalize your investment profile for tailored financial advice</p>
          </div>
        </div>

        {/* How It Works Section */}
        <h1 className='titles' style={{ textAlign: 'center' }}>How It Works</h1>
        <div className="how-it-works-container">
          <div className="step">
            <h2 className="step-title">Step 1: Choose Your Market</h2>
            <p className="step-description">
              Select your preferred market or stock indices. Access up-to-date data from multiple exchanges to begin analyzing the sectors and stocks that interest you.
            </p>
          </div>
          <div className="step">
            <h2 className="step-title">Step 2: Track Real-Time Data</h2>
            <p className="step-description">
              Monitor real-time stock prices, news updates, and market trends. Stay informed with live data that helps you keep pace with market movements.
            </p>
          </div>
          <div className="step">
            <h2 className="step-title">Step 3: Analyze & Visualize Trends</h2>
            <p className="step-description">
              Use interactive charts and graphs to explore historical data, price trends, and patterns. Identify market signals and gain deeper insights with visualized data.
            </p>
          </div>
          <div className="step">
            <h2 className="step-title">Step 4: Set Up Your Personalized Alerts</h2>
            <p className="step-description">
              Create custom alerts for stocks or market events. Get notified when stocks meet your chosen criteria, so you never miss an opportunity.
            </p>
          </div>
          <div className="step">
            <h2 className="step-title">Step 5: Make Data-Driven Predictions</h2>
            <p className="step-description">
              Leverage predictive models to forecast stock prices and potential market changes. Enhance your investment strategy with AI-driven insights and recommendations tailored to your profile.
            </p>
          </div>
        </div>
<div className="get-started-section">
          <h2 className="titles">Ready to elevate your investment strategy?</h2>
          <center>
            <a href ="http://localhost:8501/"><button className="lastbutton" style={{ fontSize: '19px', fontFamily: 'sans-serif' }}>
              Get Started
            </button></a>
          </center>
        </div>  

        

         {/* Footer Section */}
      <footer className="Footer">
        <div className="footer-top">
          <h4 style={{ color: "#94a3b8", fontSize: "10px", fontFamily: "sans-serif" }}>
            We are Data Science Students from NMAMIT, Mangaluru
          </h4>
        </div>

        <div className="footer-container">
          {/* About Us Section */}
          <div className="footer-column">
            <h3 className="Footer-title">About Us</h3>
            <ul className="Footer-list">
              <li>Sarvajith Adyanthaya</li>
              <li>Kirthan Shetty</li>
              <li>Shreevathsa Tantry</li>
              <li>Vishanth Chandan</li>
            </ul>
          </div>

          {/* Contact Us Section */}
          <div className="footer-column">
            <h3 className="Footer-title">Contact Us</h3>
            <ul className="Footer-list">
              <li>nnm22ad048@nmamit.in</li>
              <li>nnm22ad051@nmamit.in</li>
              <li>nnm22ad054@nmamit.in</li>
              <li>nnm22ad068@nmamit.in</li>
            </ul>
          </div>

          {/* Useful Links Section */}
          <div className="footer-column">
            <h3 className="Footer-title">Page Details</h3>
            <ul className="Footer-list">
              <li><a href="#features">Features</a></li>
              <li><a href="#how-it-works">How It Works</a></li>
              <li><a href="http://localhost:8501/">Get Started</a></li>
              <li><a href="#contact">Contact Us</a></li>
            </ul>
          </div>
        </div>

        {/* Copyright Notice */}
        <div className="footer-bottom">
          <p style={{ color: "#94a3b8", fontSize: "0.75rem", textAlign: "center" }}>
            &copy; {new Date().getFullYear()} Business Insight Pro. All rights reserved.
          </p>
        </div>
      </footer>
      </main>
    </div>
  );
}

export default App;