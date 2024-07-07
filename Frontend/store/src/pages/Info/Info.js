// src/pages/news/News.js
import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import Breadcrumbs from '../../components/pageProps/Breadcrumbs';
import 'bootstrap/dist/css/bootstrap.min.css';

const News = () => {
  const location = useLocation();
  const [prevLocation, setPrevLocation] = useState("");

  useEffect(() => {
    setPrevLocation(location.state?.data || ""); // Add optional chaining to avoid errors if state is undefined
  }, [location]);

  const newsArticles = [
    {
      title: "PlayStation 5: Summer Sale Extravaganza",
      content: "Grab the hottest PS5 titles at unbeatable prices during our summer sale. Discounts up to 50% off on select games and accessories!",
      link: "/shop/sale"
    },
    {
      title: "New PS5 Accessories Released",
      content: "Check out the latest PS5 accessories to enhance your gaming experience. From new controllers to VR headsets, find the perfect addition to your setup.",
      link: "/shop/accessories"
    },
    {
      title: "Exclusive PS5 Bundles Now Available",
      content: "Get the best value with our exclusive PS5 bundles, including top-rated games and essential accessories.",
      link: "/shop/bundles"
    }
  ];

  return (
    <div className="container my-5">
      <Breadcrumbs title="Journals" prevLocation={prevLocation} />
      <div className="pb-4">
        <h1 className="text-center text-primary font-weight-bold mb-4">
          PS5 E-Commerce News
        </h1>
        <div className="row">
          {newsArticles.map((article, index) => (
            <div className="col-md-4 mb-4" key={index}>
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title text-primary">{article.title}</h5>
                  <p className="card-text">{article.content}</p>
                  <Link to={article.link} className="btn btn-primary">
                    Read More
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="text-center mt-4">
          <Link to="/shop">
            <button className="btn btn-success">
              Continue Shopping
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default News;
