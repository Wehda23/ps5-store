import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import "./Desktop.css";

const Desktop = ({ className = "" }) => {
  const navigate = useNavigate();

  const onDesktopContainerClick = useCallback(() => {
    navigate("/tablet");
  }, [navigate]);

  return (
    <div className={`desktop ${className}`} onClick={onDesktopContainerClick}>
      <section className="desktop1">
        <div className="frame-parent1">
          <div className="navigation-wrapper">
            <div className="navigation">
              <a className="playstation1">PlayStation</a>
              <img
                className="ps5-logo-1-icon1"
                loading="lazy"
                alt=""
                src="/ps5logo-11@2x.png"
              />
            </div>
          </div>
          <div className="topbar">
            <a className="games1">Games</a>
            <div className="services-wrapper">
              <a className="services1">Services</a>
            </div>
            <a className="shop1">Shop</a>
            <a className="help1">Help</a>
            <a className="signin">signin</a>
            <img
              className="login-icon1"
              loading="lazy"
              alt=""
              src="/login1@2x.png"
            />
            <img className="search-icon1" alt="" src="/search@2x.png" />
            <a className="search1">Search</a>
            <img
              className="close-icon1"
              loading="lazy"
              alt=""
              src="/close1.svg"
            />
          </div>
        </div>
        <div className="leftside">
          <img
            className="logo-content-icon"
            alt=""
            src="/logo-content@2x.png"
          />
          <img
            className="playstation-icon2"
            loading="lazy"
            alt=""
            src="/playstation2@2x.png"
          />
        </div>
        <div className="desktop-inner">
          <div className="frame-parent2">
            <div className="frame-wrapper1">
              <div className="conatainer-parent">
                <div className="conatainer">
                  <div className="ps5-e-commerce-wrapper">
                    <div className="ps5-e-commerce2">Ps5 E-commerce</div>
                  </div>
                  <div className="your-gateway-to2">
                    Your Gateway to PS5 Adventure
                  </div>
                  <div className="stars1">
                    <img
                      className="stars-child"
                      loading="lazy"
                      alt=""
                      src="/star-11.svg"
                    />
                    <img
                      className="stars-item"
                      loading="lazy"
                      alt=""
                      src="/star-2.svg"
                    />
                    <img
                      className="stars-inner"
                      loading="lazy"
                      alt=""
                      src="/star-3.svg"
                    />
                  </div>
                </div>
                <div className="ps-controller-frame">
                  <img
                    className="ps-controller-icon2"
                    loading="lazy"
                    alt=""
                    src="/ps-controller1@2x.png"
                  />
                </div>
              </div>
            </div>
            <div className="cards2">
              <div className="card32">
                <img className="vector-icon" alt="" src="/vector.svg" />
                <img
                  className="joystick-icon2"
                  loading="lazy"
                  alt=""
                  src="/joystick2@2x.png"
                />
              </div>
              <div className="card22">
                <img className="vector-icon1" alt="" src="/vector-1.svg" />
                <img
                  className="controller-icon2"
                  loading="lazy"
                  alt=""
                  src="/controller2@2x.png"
                />
              </div>
              <div className="card12">
                <img className="vector-icon2" alt="" src="/vector-2.svg" />
                <img
                  className="headset-icon2"
                  loading="lazy"
                  alt=""
                  src="/headset1@2x.png"
                />
              </div>
              <div className="backforwd-arrow2">
                <img
                  className="less-than-icon2"
                  loading="lazy"
                  alt=""
                  src="/less-than2@2x.png"
                />
                <img
                  className="more-than-icon2"
                  alt=""
                  src="/more-than@2x.png"
                />
              </div>
            </div>
          </div>
        </div>
        <div className="desktop-child">
          <div className="ps-controller-parent">
            <img
              className="ps-controller-icon3"
              loading="lazy"
              alt=""
              src="/ps-controller-11@2x.png"
            />
            <div className="bottom-icon-wrapper">
              <div className="bottom-icon">
                <div className="bottom-icon-child" />
                <div className="footericon1">
                  <img
                    className="facebook-icon1"
                    loading="lazy"
                    alt=""
                    src="/facebook1@2x.png"
                  />
                  <img
                    className="youtube-logo-icon1"
                    loading="lazy"
                    alt=""
                    src="/youtube-logo1@2x.png"
                  />
                  <img
                    className="discord-new-icon1"
                    loading="lazy"
                    alt=""
                    src="/discord-new1@2x.png"
                  />
                  <img
                    className="twitterx-icon1"
                    loading="lazy"
                    alt=""
                    src="/twitterx1@2x.png"
                  />
                </div>
              </div>
            </div>
            <div className="line-wrapper">
              <div className="line">
                <img
                  className="horizontal-icon1"
                  alt=""
                  src="/horizontal1.svg"
                />
                <div className="alx-se-team-wrapper">
                  <div className="alx-se-team1">ALX_SE Team</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

Desktop.propTypes = {
  className: PropTypes.string,
};

export default Desktop;
