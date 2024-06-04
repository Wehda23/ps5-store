import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import "./Tablet.css";

const Tablet = ({ className = "" }) => {
  const navigate = useNavigate();

  const onTabletContainerClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={`tablet ${className}`} onClick={onTabletContainerClick}>
      <section className="tablet1">
        <div className="top-bar">
          <img
            className="ps5-logo-1-icon"
            loading="lazy"
            alt=""
            src="/ps5logo-1@2x.png"
          />
          <img
            className="menu-icon1"
            loading="lazy"
            alt=""
            src="/menu1@2x.png"
          />
          <div className="user-actions">
            <a className="playstation">PlayStation</a>
            <a className="games">Games</a>
            <a className="services">Services</a>
            <a className="shop">Shop</a>
            <a className="help">Help</a>
            <a className="sign-in">sign in</a>
          </div>
          <div className="search-parent">
            <img
              className="search-icon"
              loading="lazy"
              alt=""
              src="/search@2x.png"
            />
            <div className="search-label">
              <img
                className="login-icon"
                loading="lazy"
                alt=""
                src="/login@2x.png"
              />
            </div>
          </div>
          <div className="close-button">
            <a className="search">Search</a>
          </div>
          <div className="close-wrapper">
            <img
              className="close-icon"
              loading="lazy"
              alt=""
              src="/close.svg"
            />
          </div>
          <div className="hero-section">
            <img className="subtract-icon" alt="" src="/subtract.svg" />
            <div className="ps-controller-wrapper">
              <img
                className="ps-controller-icon"
                loading="lazy"
                alt=""
                src="/ps-controller@2x.png"
              />
            </div>
            <div className="controller-image-parent">
              <div className="controller-image">
                <div className="slogan-parent">
                  <div className="slogan">
                    <div className="ps5-e-commerce-parent">
                      <h1 className="ps5-e-commerce1">Ps5 E-commerce</h1>
                      <h3 className="your-gateway-to1">
                        Your Gateway to PS5 Adventure
                      </h3>
                    </div>
                    <div className="rating">
                      <img
                        className="playstation-icon1"
                        loading="lazy"
                        alt=""
                        src="/playstation1@2x.png"
                      />
                    </div>
                  </div>
                  <div className="carousel">
                    <div className="stars">
                      <img
                        className="star-icons"
                        loading="lazy"
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className="star-icons1"
                        loading="lazy"
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className="star-icons2"
                        loading="lazy"
                        alt=""
                        src="/star-1.svg"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div className="footer">
                <div className="backforwd-arrow1">
                  <img
                    className="more-than-icon1"
                    loading="lazy"
                    alt=""
                    src="/more-than1@2x.png"
                  />
                  <img
                    className="less-than-icon1"
                    loading="lazy"
                    alt=""
                    src="/less-than1@2x.png"
                  />
                </div>
                <div className="cards1">
                  <div className="card31">
                    <div className="box12" />
                    <div className="box22" />
                    <img
                      className="joystick-icon1"
                      loading="lazy"
                      alt=""
                      src="/joystick1@2x.png"
                    />
                  </div>
                  <div className="card21">
                    <div className="box31" />
                    <div className="box51" />
                    <img
                      className="controller-icon1"
                      loading="lazy"
                      alt=""
                      src="/controller1@2x.png"
                    />
                  </div>
                  <div className="card11">
                    <div className="box41" />
                    <div className="box61" />
                    <img
                      className="headset-icon1"
                      alt=""
                      src="/headset@2x.png"
                    />
                  </div>
                </div>
              </div>
              <div className="content">
                <div className="frame-div">
                  <div className="ps-controller-container">
                    <img
                      className="ps-controller-icon1"
                      loading="lazy"
                      alt=""
                      src="/ps-controller-1@2x.png"
                    />
                  </div>
                  <div className="social-icons">
                    <div className="footericon">
                      <img
                        className="facebook-icon"
                        loading="lazy"
                        alt=""
                        src="/facebook@2x.png"
                      />
                      <img
                        className="youtube-logo-icon"
                        loading="lazy"
                        alt=""
                        src="/youtube-logo@2x.png"
                      />
                      <img
                        className="twitterx-icon"
                        loading="lazy"
                        alt=""
                        src="/twitterx@2x.png"
                      />
                      <img
                        className="discord-new-icon"
                        loading="lazy"
                        alt=""
                        src="/discord-new@2x.png"
                      />
                    </div>
                  </div>
                  <div className="divider">
                    <img
                      className="horizontal-icon"
                      loading="lazy"
                      alt=""
                      src="/horizontal.svg"
                    />
                  </div>
                  <div className="team-name">
                    <div className="alx-se-team">ALX_SE Team</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="background">
          <img
            className="ps-5-icon1"
            loading="lazy"
            alt=""
            src="/ps-51@2x.png"
          />
          <div className="box23" />
        </div>
      </section>
    </div>
  );
};

Tablet.propTypes = {
  className: PropTypes.string,
};

export default Tablet;
