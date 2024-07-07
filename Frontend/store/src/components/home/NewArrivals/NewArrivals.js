import React from "react";
import Slider from "react-slick";
import Heading from "../Products/Heading";
import Product from "../Products/Product";
import {
  blackFriday,
  Controller,
  gpuconsole,
  headset,
} from "../../../assets/images/index";
import SampleNextArrow from "./SampleNextArrow";
import SamplePrevArrow from "./SamplePrevArrow";

const NewArrivals = () => {
  const settings = {
    infinite: true,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    nextArrow: <SampleNextArrow />,
    prevArrow: <SamplePrevArrow />,
    responsive: [
      {
        breakpoint: 1025,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
        },
      },
      {
        breakpoint: 769,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
        },
      },
    ],
  };
  return (
    <div className="w-full pb-16">
      <Heading heading="New Arrivals" />
      <Slider {...settings}>
        <div className="px-2">
          <Product
            _id="100001"
            img={gpuconsole}
            productName="PlayStation 5 Console"
            price="499.99"
            color="White"
            badge={true}
            des="Experience lightning-fast loading with an ultra-high-speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100002"
            img={Controller}
            productName="DualSense Wireless Controller"
            price="69.99"
            color="White"
            badge={true}
            des="Discover a deeper, highly immersive gaming experience that brings the action to life in the palms of your hands. The DualSense wireless Controller offers haptic feedback, dynamic adaptive triggers, and a built-in microphone, all integrated into an iconic comfortable design."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100003"
            img={headset}
            productName="PlayStation 5 HD Camera"
            price="59.99"
            color="White"
            badge={true}
            des="Personalize and share your gameplay. With dual lenses for 1080p capture and a built-in stand, the HD camera works seamlessly with the PS5 background removal tools to put you in the spotlight."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100004"
            img={gpuconsole}
            productName="PlayStation 5 Media Remote"
            price="29.99"
            color="White"
            badge={false}
            des="Conveniently control movies, streaming services, and more on your PS5 console with an intuitive layout."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100005"
            img={blackFriday}
            productName="PlayStation 5 Pulse 3D Wireless Headset"
            price="99.99"
            color="White"
            badge={false}
            des="Enjoy a seamless, wireless experience with a headset fine-tuned for 3D Audio on PS5 consoles. The PULSE 3D wireless headset features a refined design with dual noise-canceling microphones, built-in rechargeable battery, and an array of easy-access controls."
          />
        </div>
      </Slider>
    </div>
  );
};

export default NewArrivals;
