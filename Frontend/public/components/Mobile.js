import PropTypes from "prop-types";
import "./Mobile.css";

const Mobile = ({ className = "" }) => {
  return (
    <div className={`mobile ${className}`}>
      <section className="products-page">
        <div className="hero-background" />
        <div className="playstation-5-parent">
          <div className="playstation-5">
            <div className="box2-parent">
              <div className="box2" />
              <img
                className="ps-5-icon"
                loading="lazy"
                alt=""
                src="/ps-5@2x.png"
              />
            </div>
            <div className="playstation-5-inner">
              <div className="game-console-parent">
                <div className="game-console">Game console</div>
                <div className="playstation-5-digital-container">
                  <p className="playstation-51">Playstation 5</p>
                  <p className="digital-edition">Digital Edition</p>
                </div>
              </div>
            </div>
          </div>
          <div className="frame-wrapper">
            <div className="frame-parent">
              <div className="frame-container">
                <div className="menu-button-parent">
                  <div className="menu-button">
                    <div className="border-parent">
                      <div className="border" />
                      <div className="box" />
                    </div>
                    <img
                      className="menu-icon"
                      loading="lazy"
                      alt=""
                      src="/menu.svg"
                    />
                  </div>
                  <div className="ps5-logo-wrapper">
                    <img
                      className="ps5-logo-icon"
                      loading="lazy"
                      alt=""
                      src="/ps5-logo.svg"
                    />
                  </div>
                  <div className="settings-button-wrapper">
                    <div className="settings-button">
                      <div className="box1" />
                      <img
                        className="settings-icon"
                        loading="lazy"
                        alt=""
                        src="/settings.svg"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div className="mobile-hero">
                <div className="ps5-e-commerce">Ps5 E-commerce</div>
                <div className="your-gateway-to-ps5-adventure-wrapper">
                  <div className="your-gateway-to">
                    Your Gateway to PS5 Adventure
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="stars-wrapper">
          <img className="stars-icon" alt="" src="/stars.svg" />
        </div>
        <div className="frame-group">
          <div className="cards-wrapper">
            <div className="cards">
              <div className="card3">
                <div className="box11" />
                <div className="box2-group">
                  <div className="box21" />
                  <img
                    className="joystick-icon"
                    loading="lazy"
                    alt=""
                    src="/joystick@2x.png"
                  />
                </div>
              </div>
              <div className="card2">
                <div className="box3" />
                <div className="box5-parent">
                  <div className="box5" />
                  <img
                    className="controller-icon"
                    loading="lazy"
                    alt=""
                    src="/controller@2x.png"
                  />
                </div>
              </div>
              <div className="card1">
                <div className="box6" />
                <div className="box4-parent">
                  <div className="box4" />
                  <img
                    className="headset-icon"
                    loading="lazy"
                    alt=""
                    src="/headset@2x.png"
                  />
                </div>
              </div>
              <div className="middle-txt">
                <div className="headset">Headset</div>
                <div className="control">control</div>
                <div className="joystick">joystick</div>
              </div>
            </div>
          </div>
          <img
            className="menu-block-icon"
            loading="lazy"
            alt=""
            src="/menu-block.svg"
          />
        </div>
      </section>
      <div className="backforwd-arrow">
        <img
          className="less-than-icon"
          loading="lazy"
          alt=""
          src="/less-than@2x.png"
        />
        <div className="more-than-wrapper">
          <img
            className="more-than-icon"
            loading="lazy"
            alt=""
            src="/more-than@2x.png"
          />
        </div>
      </div>
      <div className="mobile-inner">
        <div className="playstation-parent">
          <img
            className="playstation-icon"
            loading="lazy"
            alt=""
            src="/playstation@2x.png"
          />
          <img className="mobile-icon" alt="" src="/mobile.svg" />
        </div>
      </div>
    </div>
  );
};

Mobile.propTypes = {
  className: PropTypes.string,
};

export default Mobile;
