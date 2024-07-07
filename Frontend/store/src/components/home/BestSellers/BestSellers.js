import React from "react";
import Heading from "../Products/Heading";
import Product from "../Products/Product";
import {
  gpuconsole,
  headset2,
  ps5Console,
  sonNewPs5,
} from "../../../assets/images/index";

const BestSellers = () => {
  return (
    <div className="w-full pb-20">
      <Heading heading="Our Bestsellers" />
      <div className="w-full grid grid-cols-1 md:grid-cols-2 lgl:grid-cols-3 xl:grid-cols-4 gap-10">
        <Product
          _id="1011"
          img={ps5Console}
          productName="PlayStation 5 Console"
          price="499.99"
          color="White"
          badge={true}
          des="Experience lightning-fast loading with an ultra-high-speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games."
        />
        <Product
          _id="1012"
          img={headset2}
          productName="DualSense Wireless Controller"
          price="69.99"
          color="White"
          badge={false}
          des="Discover a deeper, highly immersive gaming experience with the innovative new PS5 controller, featuring haptic feedback and dynamic trigger effects."
        />
        <Product
          _id="1013"
          img={sonNewPs5}
          productName="Pulse 3D Wireless Headset"
          price="99.99"
          color="White"
          badge={true}
          des="Enjoy a seamless, wireless experience with a headset fine-tuned for 3D Audio on PS5 consoles."
        />
        <Product
          _id="1014"
          img={gpuconsole}
          productName="PS5 HD Camera"
          price="59.99"
          color="Black"
          badge={false}
          des="Add yourself to your gameplay videos and broadcasts with smooth, sharp full-HD capture."
        />
      </div>
    </div>
  );
};

export default BestSellers;
