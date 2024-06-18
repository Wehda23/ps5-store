import {
  sonNewPs5,
  vr3Dheadset2,
  vr3Dheadset,
  sony_ps_vr_01,
  vantageControl,
  blackFriday,
  Controller,
  gpuconsole,
  headset,
  bwControl,
  pdf1,
  ps5sony,

  game,
  sandLand,
  game3,
  sonyPlayStationPS5,
  cleaningKit,
  headset2,
  ps5Console,
  ps5LEDSlimcopy,
  helldiver,
  ps5black,
  sansungGalaxyGaming,
  nacon144,
  naconRevolution,
  ps5headset,
  ps5sipederman,
  blueGamepad,
  RedSony,
  horizon,
  horizon1,
  spiderman,
  godWar,
  ratchet,
  right1copy,
  ps5usb,
} from "../assets/images/index";

import "./style.css";

// =================== NavBarList Start here ====================
export const navBarList = [
  {
    _id: 1001,
    title: "PlayStation5",
    link: "/",
  },
  {
    _id: 1006,
    title: "Games",
    link: "/",
  },
  {
    _id: 1007,
    title: "services",
    link: "/",
  },
  {
    _id: 1002,
    title: "Shop",
    link: "/shop",
  },
  {
    _id: 1003,
    title: "Help",
    link: "/Help",
  },
  {
    _id: 1004,
    title: "Contact",
    link: "contact",
  },
  {
    _id: 1005,
    title: "News",
    link: "/Info",
  },
];
// =================== NavBarList End here ======================
// =================== Special Offer data Start here ============
export const SplOfferData = [
  {
    _id: "201",
    img: sonNewPs5,
    productName: "DualSense Wireless Controller",
    price: "69.99",
    color: "White",
    badge: false,
    des: "Discover a deeper, highly immersive gaming experience with the innovative new PS5 controller, featuring haptic feedback and dynamic trigger effects.",
    cat: "Controller",
  },
  {
    _id: "202",
    img: "horizon",
    productName: "PlayStation 5 Console",
    price: "499.99",
    color: "White",
    badge: true,
    des: "Experience lightning-fast loading with an ultra-high-speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games.",
    cat: "Console",
  },
  {
    _id: "203",
    img: "horizon2", // Replace with the new image path for PS5 headset
    productName: "PULSE 3D Wireless Headset",
    price: "99.99",
    color: "White",
    badge: false,
    des: "Enjoy a seamless, wireless experience with a headset fine-tuned for 3D Audio on PS5 consoles. Features a sleek design and dual noise-cancelling microphones.",
    cat: "Accessory",
  },
  {
    _id: "204",
    img: "bwControl",
    productName: "HD Camera",
    price: "59.99",
    color: "Black",
    badge: false,
    des: "Add yourself to your gameplay videos and broadcasts with smooth, sharp full-HD capture, featuring dual wide-angle lenses.",
    cat: "Accessory",
  },
  {
    _id: "205",
    img: "ps5_media_remote.jpg", // Replace with the new image path for PS5 media remote
    productName: "Media Remote",
    price: "29.99",
    color: "White",
    badge: false,
    des: "Conveniently control movies, streaming services, and more on your PS5 console with an intuitive layout.",
    cat: "Accessory",
  },
  {
    _id: "206",
    img: "ps5_charging_station.jpg",
    productName: "DualSense Charging Station",
    price: "29.99",
    color: "White",
    badge: false,
    des: "Charge up to two DualSense wireless controllers simultaneously without having to connect them to your PlayStation 5 console.",
    cat: "Accessory",
  },
  {
    _id: "207",
    img: "vantageControl",
    productName: "Spider-Man: Miles Morales",
    price: "49.99",
    color: "Mixed",
    badge: true,
    des: "Experience the rise of Miles Morales as the new hero masters incredible, explosive new powers to become his own Spider-Man.",
    cat: "Game",
  },
  {
    _id: "208",
    img: "ps5_game_demon_souls.jpg", // Replace with the new image path for Demon's Souls game
    productName: "Demon's Souls",
    price: "69.99",
    color: "Mixed",
    badge: true,
    des: "Discover where the journey began with this stunningly beautiful remake of the PlayStation classic, Demon’s Souls.",
    cat: "Game",
  },
  {
    _id: "209",
    img: "ps5_game_ratchet_clank.jpg", // Replace with the new image path for Ratchet & Clank game
    productName: "Ratchet & Clank: Rift Apart",
    price: "69.99",
    color: "Mixed",
    badge: true,
    des: "Blast your way through an interdimensional adventure with Ratchet and Clank as they take on an evil emperor from another reality.",
    cat: "Game",
  },
  {
    _id: "210",
    img: "ps5_game_returnal.jpg", // Replace with the new image path for Returnal game
    productName: "Returnal",
    price: "69.99",
    color: "Mixed",
    badge: true,
    des: "Break the cycle of chaos on an always-changing alien planet in this third-person roguelike shooter.",
    cat: "Game",
  },
];

// =================== Special Offer data End here ==============

// =================== PaginationItems Start here ===============

export const paginationItems = [
  {
    _id: "201",
    img: vantageControl,
    productName: "DualSense Wireless Controller",
    price: "69.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Experience the modernized design of the PS5 DualSense Wireless Controller, featuring haptic feedback, adaptive triggers, a built-in microphone, and a dedicated Create button. The DualSense controller offers immersive gaming with enhanced features and comfort.",
    cat: "Controller",
    pdf: Controller,
    ficheTech: [
      { label: "Compatibility", value: "PlayStation 5" },
      { label: "Connectivity", value: "USB Type-C, Bluetooth 5.1" },
      { label: "Battery Life", value: "Up to 12 hours" },
      { label: "Color Options", value: "White, Midnight Black, Cosmic Red, Starlight Blue" },
      { label: "Features", value: "Haptic feedback, Adaptive triggers, Built-in microphone" }
    ],
  },
  {
    _id: "202",
    img: gpuconsole,
    productName: "PlayStation 5 Console",
    price: "499.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "The PlayStation 5 Console unleashes new gaming possibilities that you never anticipated. Experience lightning-fast loading with an ultra-high speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games.",
    cat: "Console",
    pdf: pdf1,
    ficheTech: [
      { label: "CPU", value: "8x Zen 2 Cores at 3.5GHz" },
      { label: "GPU", value: "10.28 TFLOPs, 36 CUs at 2.23GHz, RDNA 2 architecture" },
      { label: "RAM", value: "16GB GDDR6/256-bit" },
      { label: "Storage", value: "825GB Custom NVMe SSD" },
      { label: "Expansion", value: "NVMe SSD Slot" },
      { label: "Optical Drive", value: "Ultra HD Blu-ray" },
      { label: "Resolution", value: "Up to 8K" },
      { label: "Frame Rate", value: "Up to 120 fps" },
      { label: "Backward Compatibility", value: "PS4 games and accessories" }
    ],
  },
  {
    _id: "203",
    img: vantageControl,
    productName: "Pulse 3D Wireless Headset",
    price: "99.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "The Pulse 3D Wireless Headset is designed to deliver the 3D Audio made possible by the PlayStation 5 console. Enjoy a seamless, wireless experience with a headset fine-tuned for 3D Audio on PS5 consoles.",
    cat: "Headset",
    pdf: pdf1,
    ficheTech: [
      { label: "Compatibility", value: "PlayStation 5, PlayStation 4, PC" },
      { label: "Battery Life", value: "Up to 12 hours" },
      { label: "Microphone", value: "Dual hidden microphones" },
      { label: "Audio", value: "Tempest 3D AudioTech" },
      { label: "Connectivity", value: "Wireless adapter, 3.5mm jack" }
    ],
  },
  {
    _id: "204",
    img: vantageControl,
    productName: "HD Camera",
    price: "59.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Add yourself to your gameplay videos and broadcasts with smooth, sharp, full-HD capture with the PS5 HD Camera. With dual wide-angle lenses and a built-in stand, capture your moments in Full-HD 1080p.",
    cat: "Camera",
    pdf: pdf1,
    ficheTech: [
      { label: "Resolution", value: "1080p" },
      { label: "Lens", value: "Dual wide-angle lenses" },
      { label: "Connectivity", value: "USB Type-A" },
      { label: "Built-in Stand", value: "Yes" },
      { label: "Compatibility", value: "PlayStation 5" }
    ],
  },
  {
    _id: "205",
    img: blackFriday,
    productName: "Media Remote",
    price: "29.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Conveniently control movies, streaming services, and more on your PS5 console with an intuitive layout featuring media controls. The PS5 Media Remote is the perfect companion for your entertainment needs.",
    cat: "Remote",
    pdf: pdf1,
    ficheTech: [
      { label: "Compatibility", value: "PlayStation 5" },
      { label: "Battery", value: "2 x AA batteries (included)" },
      { label: "Connectivity", value: "Infrared" },
      { label: "Features", value: "Play, Pause, Fast forward, and more" }
    ],
  },
  {
    _id: "206",
    img: headset,
    productName: "DualSense Charging Station",
    price: "29.99",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Charge up to two DualSense wireless controllers simultaneously without having to connect them to your PlayStation 5 console. The DualSense Charging Station allows you to keep your controllers organized and ready for use.",
    cat: "Accessory",
    pdf: pdf1,
    ficheTech: [
      { label: "Compatibility", value: "DualSense Wireless Controllers" },
      { label: "Capacity", value: "2 controllers" },
      { label: "Power Supply", value: "AC Adapter" },
      { label: "Color Options", value: "White" },
      { label: "Features", value: "Fast charging" }
    ],
  },

  {
    _id: "207",
    img: bwControl,
    productName: "IMPRIMANTE PANTUM P3300DW",
    price: "450",
    color: "Blanc",
    badge: true,
    brand: "Pantum",
    des: "Imprimante Laser PANTUM P3300DW - Fonctions: Impression - Technologie d'impression: Laser - Format Papier: A4-A5 - Vitesse d’impression: 33 ppm (A4) / 35 ppm (Lettre) - Résolution d'impression: Jusqu'à 1200 x 1200 ppp - Papier Bac d'alimentation: 250 pages - Sortie papier: 150 page - Mémoire: 256 Mo - Impression recto verso: Automatique - Heure de la première impression: Moins de 8.2s - Interface: Ethernet USB 2.0 haut débit : Wi-Fi IEEE 802.3 10/100Base-Tx : IEEE 802.11b/g/n - Connecteurs: USB ; WIFI - Dimensions: 354 x 334 x 232mm - Poids: 6,8 kg - Couleur: Blanc",
    cat: "Imprimante",
    pdf: pdf1,
    ficheTech: [
      { label: "gtin		", value: "P3300DW      " },
      { label: "fonctions	", value: "Monofonction      " },
      { label: "Mémoire	", value: "256 Mo      " },
      { label: "Technologie d impression		", value: "Laser      " },
      { label: "Connectivite	", value: "WIFI      " },
      { label: "Vitesse du Processeur		", value: "350 MHz      " },
      { label: "Type ecran		", value: "LCD 2 lignes      " },
      {
        label: "Consommation d énergie		",
        value:
          "Impression : 525 W en moyenne Veille : 50 W en veille : moins de 2 W      ",
      },
      {
        label: "Gestion d entrée Papier Standard		",
        value: "Papier Bac d'alimentation: 250pages      ",
      },
      { label: "Premiére Page Imprimée		", value: "Moins de 8,2 secondes      " },
      {
        label: "Vitesse d impression Noir		",
        value: "33 ppm (A4) / 35 ppm (Lettre)      ",
      },
      { label: "Cycle d utilisation Mensuel		", value: "60000pages      " },
      { label: "Résolution d impression		", value: "Max.1200x1200 dpi      " },
      {
        label: "Volume de Pages Mensuel Recommandé		",
        value: "750 à 3 500 pages      ",
      },
      {
        label: "Interface Réseau	",
        value:
          "Ethernet USB 2.0 haut débit : Wi-Fi IEEE 802.3 10/100Base-Tx : IEEE 802.11b/g/n      ",
      },
      {
        label: "Contenu de L'emballage		",
        value:
          "Imprimante - Cordon d’alimentation - Câble d’interface USB - Plateau de sortie - CD-ROM - Guide de configuration rapide      ",
      },
      { label: "Garantie	", value: "1 ANS      " },
    ],
  },

  {
    _id: "208",
    img: horizon,
    productName: "Spider-Man: Miles Morales",
    price: "450",
    color: "Blanc",
    badge: true,
    brand: "Pantum",
    des: "Experience the rise of Miles Morales as the new hero masters incredible, explosive new powers to become his own Spider-Man.",
    cat: "PS5 Game",
    pdf: pdf1,
    ficheTech: [
      { label: "gtin", value: "P2509W" },
      { label: "fonctions", value: "Monofonction" },
      { label: "Technologie d'impression", value: "Laser" },
      { label: "Ecran Tactile", value: "Non" },
      { label: "Connectivite", value: "WiFi" },
      { label: "Vitesse du Processeur", value: "600MHz" },
      {
        label: "Capacité papier",
        value: "Capacité standard: 1 600 pages"
      },
      { label: "Premiére Page Imprimée", value: "Moins de 7.8s" },
      { label: "Cycle d'utilisation Mensuel", value: "15 000 pages" },
      {
        label: "Résolution d'impression",
        value: "Max. 1 200 × 1 200 ppp"
      },
      { label: "formats", value: "A4" },
      { label: "Connecteurs", value: "USB 2.0, Wi-Fi" },
      {
        label: "Vitesse de Copie Noir Blanc",
        value: "22 ppm (A4) / 23 ppm (Lettre)"
      },
      {
        label: "Contenu de L'emballage",
        value:
          "Imprimante - Cordon d’alimentation - Câble d’interface USB - Plateau de sortie - CD-ROM - Guide de configuration rapide"
      },
      { label: "Dimensions", value: "337 x 220 x 178 mm" }
    ]
  },
  {
    _id: "233",
    img: horizon1,
    productName: "Ratchet & Clank: Rift Apart",
    price: "450",
    color: "Blanc",
    badge: true,
    brand: "Pantum",
    des: "Blast your way through an interdimensional adventure with Ratchet and Clank as they face an evil emperor from another reality.",
    cat: "PS5 Game",
    pdf: pdf1,
    ficheTech: []
  },
  {
    _id: "220",
    img: ratchet,
    productName: "Assassin's Creed Valhalla",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Become Eivor, a legendary Viking warrior on a quest for glory. Explore England's Dark Ages as you raid your enemies, grow your settlement, and build your political power.",
    cat: "PS5 Game"
  },
  {
    _id: "221",
    img: right1copy,
    productName: "Sandland",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "In a desolate world where both humans and demons suffer from an extreme water shortage, a small-town sheriff teams up with a demon prince to uncover a hidden reservoir.",
    cat: "PS5 Game"
  },
  {
    _id: "215",
    img: ps5Console,
    productName: "PS5 DualSense Wireless Controller",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Discover a deeper, highly immersive gaming experience with the innovative new PS5 controller, featuring haptic feedback and dynamic adaptive triggers.",
    cat: "PS5 Accessory"
  },
  {
    _id: "216",
    img: helldiver,
    productName: "PS5 HD Camera",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "With dual lenses for 1080p capture and a built-in stand, the HD camera works seamlessly with the PS5 background removal tools to put you in the spotlight.",
    cat: "PS5 Accessory"
  },
  {
    _id: "209",
    img: sony_ps_vr_01,
    productName: "PS5 Media Remote",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Conveniently control movies, streaming services and more on your PS5 console with an intuitive layout.",
    cat: "PS5 Accessory"
  },
  {
    _id: "210",
    img: vr3Dheadset2,
    productName: "PlayStation VR2 Headset",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Experience new sensations with stunning 4K HDR visuals, new sensory features and enhanced tracking with the PS VR2.",
    cat: "PS5 Accessory"
  },
  {
    _id: "211",
    img: vr3Dheadset,
    productName: "PS5 3D Wireless Headset",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Immerse yourself in the gaming experience with the PS5 wireless headset, offering 3D Audio support and dual noise-cancelling microphones.",
    cat: "PS5 Accessory"
  },
  {
    _id: "212",
    img: ps5Console,
    productName: "PS5 DualSense Charging Station",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Charge up to two DualSense wireless controllers simultaneously without having to connect them to your PS5 console.",
    cat: "PS5 Accessory"
  },
  {
    _id: "213",
    img: cleaningKit,
    productName: "PS5 Console Cover",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Personalize your PlayStation 5 console with a new cover designed to replace the original white faceplates.",
    cat: "PS5 Accessory"
  },
  {
    _id: "214",
    img: ps5black,
    productName: "PS5 Vertical Stand",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Secure your PS5 console in a vertical position with this durable stand designed specifically for the console.",
    cat: "PS5 Accessory"
  },
  {
    _id: "217",
    img: sansungGalaxyGaming,
    productName: "PS5 Cooling Fan",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Keep your PS5 console cool during intense gaming sessions with this efficient cooling fan.",
    cat: "PS5 Accessory"
  },
  {
    _id: "219",
    img: godWar,
    productName: "PS5 Game Storage Tower",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Organize and store your PS5 game cases and accessories with this sleek and sturdy storage tower.",
    cat: "PS5 Accessory"
  },


  // =================== imprimante hp =================

  {
    _id: "hp1",
    img: ps5sony,
    productName: "Backward Compatible PS5",
    price: "450",
    color: "Blanc",
    badge: true,
    brand: "Sony",
    des: "Desc : Play your favorite PS4 games on the PS5 console with stunning performance enhancements. The PS5 console is backward compatible with the overwhelming majority of PS4 games.",
    cat: "PS5 Accessory",
    pdf: pdf1,
    ficheTech: [
      { label: "DISPONIBILITÉ", value: "En stock" },
      { label: "gtin", value: "3YW70A" },
      { label: "Marque", value: "Sony" },
      { label: "Destockage", value: "Non" },
      { label: "Ecran", value: "LCD" },
      {
        label: "Taille de L'écran cm",
        value: "Affichage LCD 7 segments + icône 5,08 cm (2 pouces)"
      },
      { label: "Ecran Tactile", value: "Non" },
      { label: "Technologie d'impression", value: "Jet d'encre" },
      { label: "fonctions", value: "Multifonction" },
      { label: "Fonctionnalités", value: "Impression, Copie, Numérisation" },
      { label: "Impression", value: "Couleur" },
      { label: "formats", value: "A4" },
      { label: "Chargement de Documents", value: "Oui" },
      { label: "Vitesse d'impression Noir", value: "Jusqu'à 22 ppm" },
      { label: "Vitesse d'impression Couleur", value: "Jusqu'à 16 ppm" },
      { label: "FAX", value: "Non" },
      { label: "Mémoire", value: "256 Mo" },
      {
        label: "Qualité d'impression Noir",
        value: "Jusqu'à 1 200 x 1 200 ppp"
      },
      {
        label: "Qualité d'impression Couleur",
        value: "Jusqu'à 4 800 x 1 200 ppp"
      },
      { label: "Résolution d'impression Couleur", value: "1200x1200dpi" },
      { label: "Recto/Verso", value: "Manuel" },
      { label: "Type de Scanner", value: "Scanner à Plat" },
      { label: "Connectivite", value: "USB 2.0, WiFi" },
      { label: "Capacité papier", value: "100 feuilles" },
      { label: "Cycle d'utilisation Mensuel", value: "Jusqu'à 1000 pages" },
      {
        label: "Consommation électrique",
        value: "0,12 Watts (Arrêt manuel), 3,12 Watts (Prêt), 0,75 Watt (Veille) 5"
      },
      { label: "Grammage", value: "75 g/m²" },
      {
        label: "Contenu de L'emballage",
        value: "PlayStation 5 console, DualSense wireless controller, Base, HDMI cable, AC power cord, USB cable, Printed materials"
      },
      { label: "Poids", value: "5,14 kg" },
      { label: "Dimensions", value: "447 x 373 x 158 mm" },
      { label: "Couleur", value: "Blanc" },
      { label: "Garantie", value: "1 an" }
    ]
  },
  {
    _id: "hp2",
    img: blueGamepad,
    productName: "PlayStation Collectibles",
    price: "450",
    color: "Blanc",
    badge: true,
    brand: "Sony",
    des: "Desc : Collect exclusive PlayStation-themed memorabilia including figures, posters, and other unique items that celebrate the legacy and history of PlayStation.",
    cat: "PS5 Accessory",
    pdf: pdf1,
    ficheTech: []
  },
  {
    _id: "215",
    img: ps5LEDSlimcopy,
    productName: "Pro Tech Toolkit",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "This comprehensive toolkit is perfect for repairs and upgrades, featuring high-quality tools for all your technical needs.",
    cat: "PS5 Accessory"
  },
  {
    _id: "216",
    img: headset2,
    productName: "PS5 HD Camera",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "With dual lenses for 1080p capture and a built-in stand, the HD camera works seamlessly with the PS5 background removal tools to put you in the spotlight.",
    cat: "PS5 Accessory"
  },
  {
    _id: "209",
    img: sony_ps_vr_01,
    productName: "PS5 Media Remote",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Conveniently control movies, streaming services and more on your PS5 console with an intuitive layout.",
    cat: "PS5 Accessory"
  },
  {
    _id: "210",
    img: vr3Dheadset2,
    productName: "PlayStation VR2 Headset",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Experience new sensations with stunning 4K HDR visuals, new sensory features and enhanced tracking with the PS VR2.",
    cat: "PS5 Accessory"
  },
  {
    _id: "211",
    img: vr3Dheadset,
    productName: "PS5 3D Wireless Headset",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Immerse yourself in the gaming experience with the PS5 wireless headset, offering 3D Audio support and dual noise-cancelling microphones.",
    cat: "PS5 Accessory"
  },
  {
    _id: "212",
    img: ps5sipederman,
    productName: "PS5 DualSense Charging Station",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Charge up to two DualSense wireless controllers simultaneously without having to connect them to your PS5 console.",
    cat: "PS5 Accessory"
  },
  {
    _id: "213",
    img: sonNewPs5,
    productName: "PS5 Console Cover",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Personalize your PlayStation 5 console with a new cover designed to replace the original white faceplates.",
    cat: "PS5 Accessory"
  },
  {
    _id: "214",
    img: sansungGalaxyGaming,
    productName: "PS5 Vertical Stand",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Secure your PS5 console in a vertical position with this durable stand designed specifically for the console.",
    cat: "PS5 Accessory"
  },
  {
    _id: "217",
    img: spiderman,
    productName: "PS5 Cooling Fan",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Keep your PS5 console cool during intense gaming sessions with this efficient cooling fan.",
    cat: "PS5 Accessory"
  },
  {
    _id: "219",
    img:  ps5usb,
    productName: "PS5 Game Storage Tower",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Organize and store your PS5 game cases and accessories with this sleek and sturdy storage tower.",
    cat: "PS5 Accessory"
  },
  {
    _id: "hp3",
    img: RedSony,
    productName: "PlayStation VR Aim Controller",
    price: "450",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Desc: Enhance your PlayStation VR experience with precise and immersive controls with the VR Aim Controller, featuring built-in motion sensors and an ergonomic design.",
    cat: "PS5 Accessory",
    pdf: pdf1,
    ficheTech: [
      { label: "DISPONIBILITÉ", value: "En stock" },
      { label: "gtin", value: "Z4B04A" },
      { label: "Marque", value: "Sony" },
      { label: "Destockage", value: "Non" },
      { label: "Technologie d'impression", value: "Multifonction Jet d'encre" },
      { label: "fonctions", value: "Multifonction" },
      { label: "Impression", value: "Couleur" },
      { label: "Mémoire", value: "Non" },
      { label: "FAX", value: "Non" },
      { label: "Fonctionnalités", value: "Impression, Copie, Numérisation" },
      { label: "Chargement de Documents", value: "Oui" },
      { label: "Connecteurs", value: "1 port USB 2.0 haut débit" },
      { label: "Vitesse du Processeur", value: "360 MHz" },
      {
        label: "Impression sans bordure",
        value: "Oui, jusqu’à 210 x 297 mm (A4)"
      },
      { label: "Vitesse d'impression Noir", value: "Jusqu'à 19 ppm" },
      { label: "Vitesse d'impression Couleur", value: "Jusqu'à 15 ppm" },
      {
        label: "Résolution d'impression Noir",
        value: "Jusqu'à 1 200 x 1 200 DPI"
      },
      {
        label: "Résolution d'impression Couleur",
        value: "Jusqu'à 4 800 x 1 200 DPI (couleur)"
      },
      {
        label: "Résolution d'impression",
        value: "Jusqu'à 1 200 x 1 200 DPI (noir), Jusqu'à 4 800 x 1 200 DPI (couleur)"
      },
      { label: "Type de Scanner", value: "Scanner à Plat" },
      { label: "Vitesse de numérisation", value: "Jusqu'à 21 secondes" },
      { label: "Résolution de Numérisation", value: "Jusqu'à 1200 x 1200 ppp" },
      {
        label: "Résolution de numérisation optimisée",
        value: "Jusqu’à 1200 ppp"
      },
      { label: "Recto/Verso", value: "Manuel" },
      { label: "Connectivite", value: "USB" },
      { label: "formats", value: "A4" },
      {
        label: "Première Page Imprimée",
        value: "Noir: (A4, prêt) Vitesse : 14 s - Couleur (A4, prêt) Vitesse : 18 s"
      },
      {
        label: "Alimentation-courant",
        value: "Tension d'entrée : 220 à 240 V CA (+/- 10 %), 50/60 Hz (+/- 3 Hz)"
      },
      {
        label: "Type de Papier pris en charge",
        value: "Papier ordinaire, papiers photo HP, papier mat pour brochure HP ou papier professionnel HP, papier mat pour présentation HP, papier brillant pour brochure HP ou papier professionnel HP, papiers photo jet d'encre, papiers mats jet d'encre, papiers brillant"
      },
      {
        label: "Consommation électrique",
        value: "10 W maximum, 0,07 W (Arrêt), 2,1 W (Veille), 0,88 W (Veille prolongée)"
      },
      {
        label: "Cycle d'utilisation Mensuel",
        value: "A4: Jusqu'à 1 000 pages - Lettre: Jusqu'à 1 000 pages"
      },
      {
        label: "Alimentation papier standard",
        value: "Bac d'alimentation de 60 feuilles - Bac de sortie de 25 feuilles"
      },
      { label: "Ecran Tactile", value: "Non" },
      { label: "Type écran", value: "7 segments et icône LCD" },
      {
        label: "Volume de Pages Mensuel Recommandé",
        value: "400 à 800 (Jusqu'à 1000 pages)"
      },
      { label: "Interfaces standard", value: "1x port USB 2.0 haut débit" },
      { label: "Résolution optique", value: "Jusqu'à 1200 x 1200 ppp" },
      { label: "Grammage", value: "75 g/m²" },
      {
        label: "Contenu de L'emballage",
        value: "PlayStation VR Aim Controller, USB cable, Instruction manual"
      },
      { label: "Poids", value: "4,67 kg" },
      { label: "Couleur", value: "White" },
      { label: "Dimensions", value: "525 x 310 x 158 mm" },
      { label: "Garantie", value: "1 an" }
    ]
  },
  {
    _id: "218",
    img: nacon144,
    productName: "PlayStation Pulse 3D Wireless Headset",
    price: "450",
    color: "Black",
    badge: true,
    brand: "Sony",
    des: "Desc: Enjoy a seamless, wireless experience with a headset fine-tuned for 3D Audio on PS5 consoles. The PULSE 3D wireless headset features a refined design with dual noise-cancelling microphones.",
    cat: "PS5 Accessory",
    pdf: pdf1,
    ficheTech: [
      { label: "DISPONIBILITÉ", value: "En stock" },
      { label: "Marque", value: "Sony" },
      { label: "Destockage", value: "Non" },
      { label: "Technologie d'impression", value: "3D Audio" },
      { label: "fonctions", value: "Wireless" },
      { label: "Impression", value: "Audio" },
      { label: "Mémoire", value: "Non" },
      { label: "FAX", value: "Non" },
      { label: "Fonctionnalités", value: "Audio, Microphone" },
      { label: "Chargement de Documents", value: "Non" },
      { label: "Connecteurs", value: "USB-C, 3.5mm jack" },
      { label: "Vitesse du Processeur", value: "N/A" },
      {
        label: "Impression sans bordure",
        value: "N/A"
      },
      { label: "Vitesse d'impression Noir", value: "N/A" },
      { label: "Vitesse d'impression Couleur", value: "N/A" },
      {
        label: "Résolution d'impression Noir",
        value: "N/A"
      },
      {
        label: "Résolution d'impression Couleur",
        value: "N/A"
      },
      {
        label: "Résolution d'impression",
        value: "N/A"
      },
      { label: "Type de Scanner", value: "N/A" },
      { label: "Vitesse de numérisation", value: "N/A" },
      { label: "Résolution de Numérisation", value: "N/A" },
      {
        label: "Résolution de numérisation optimisée",
        value: "N/A"
      },
      { label: "Recto/Verso", value: "N/A" },
      { label: "Connectivite", value: "USB, Wireless" },
      { label: "formats", value: "N/A" },
      {
        label: "Première Page Imprimée",
        value: "N/A"
      },
      {
        label: "Alimentation-courant",
        value: "N/A"
      },
      {
        label: "Type de Papier pris en charge",
        value: "N/A"
      },
      {
        label: "Consommation électrique",
        value: "N/A"
      },
      {
        label: "Cycle d'utilisation Mensuel",
        value: "N/A"
      },
      {
        label: "Alimentation papier standard",
        value: "N/A"
      },
      { label: "Ecran Tactile", value: "Non" },
      { label: "Type écran", value: "N/A" },
      {
        label: "Volume de Pages Mensuel Recommandé",
        value: "N/A"
      },
      { label: "Interfaces standard", value: "USB-C, 3.5mm jack" },
      { label: "Résolution optique", value: "N/A" },
      { label: "Grammage", value: "N/A" },
      {
        label: "Contenu de L'emballage",
        value: "Pulse 3D Wireless Headset, Wireless adapter, USB-C charging cable, Audio cable, Instruction manual"
      },
      { label: "Poids", value: "294g" },
      { label: "Couleur", value: "Black" },
      { label: "Dimensions", value: "172 x 92 x 191 mm" },
      { label: "Garantie", value: "1 an" }
    ]
  },
  {
    _id: "220",
    img: sandLand,
    productName: "PS5 Controller Skin",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Personalize and protect your DualSense controller with a durable and stylish skin. Available in various designs and colors.",
    cat: "PS5 Accessory"
  },
  {
    _id: "229",
    img: naconRevolution,
    productName: "PS5 Wireless Charging Station",
    price: "220.00",
    color: "Black",
    badge: true,
    des: "Keep your controllers and other devices charged with this sleek wireless charging station, designed for convenience and efficiency.",
    cat: "PS5 Accessory"
  },
  {
    _id: "222",
    img: game3,
    productName: "PS5 Game Disc Case",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Organize and protect your PS5 game discs with this durable case, featuring a compact design and easy access slots.",
    cat: "PS5 Accessory"
  },
  {
    _id: "223",
    img: ps5Console,
    productName: "PS5 Screen Protector",
    price: "220.00",
    color: "Clear",
    badge: true,
    des: "Keep your PS5 display free from scratches and smudges with this high-quality screen protector, designed for easy application and maximum clarity.",
    cat: "PS5 Accessory"
  },
  {
    _id: "224",
    img: sonyPlayStationPS5,
    productName: "PS5 Controller Thumb Grips",
    price: "25.00",
    color: "Mixed",
    badge: true,
    des: "Improve your gaming precision and comfort with these durable thumb grips, designed to fit perfectly on your DualSense controller.",
    cat: "PS5 Accessory"
  },
  // =================== imprimante ricoh =================
    {
      _id: "ps5_1",
      img: cleaningKit,
      productName: "PlayStation 5",
      price: "499",
      color: "White",
      badge: true,
      brand: "Sony",
      des: "The PlayStation 5 (PS5) is a home video game console developed by Sony Interactive Entertainment. The PS5 was announced in 2019 as the successor to the PlayStation 4. It was released on November 12, 2020, in Australia, Japan, South Korea, and North America, and on November 19, 2020, in the rest of the world.",
      cat: "Console",
      pdf: pdf1,
      ficheTech: [
        { label: "Availability", value: "In stock" },
        { label: "Model Number", value: "CFI-1000A01" },
        { label: "Brand", value: "Sony" },
        { label: "Discount", value: "No" },
        { label: "Technology", value: "Custom AMD RDNA 2" },
        { label: "Functions", value: "Gaming, Streaming, Media Playback" },
        { label: "Color Output", value: "Full Color" },
        { label: "Memory", value: "16GB GDDR6" },
        { label: "Bluetooth", value: "Yes" },
        { label: "Features", value: "4K Gaming, HDR, Ray Tracing" },
        { label: "Document Loading", value: "Not Applicable" },
        { label: "Connectors", value: "HDMI, USB-C, USB-A" },
        { label: "Processor Speed", value: "3.5 GHz (variable frequency)" },
        { label: "Borderless Printing", value: "Not Applicable" },
        { label: "Black and White Speed", value: "Not Applicable" },
        { label: "Color Speed", value: "Not Applicable" },
        { label: "Black and White Resolution", value: "Not Applicable" },
        { label: "Color Resolution", value: "Not Applicable" },
        { label: "Printing Resolution", value: "Not Applicable" },
        { label: "Scanner Type", value: "Not Applicable" },
        { label: "Scan Speed", value: "Not Applicable" },
        { label: "Scan Resolution", value: "Not Applicable" },
        { label: "Optimized Scan Resolution", value: "Not Applicable" },
        { label: "Duplex Printing", value: "Not Applicable" },
        { label: "Connectivity", value: "Wi-Fi, Ethernet, Bluetooth" },
        { label: "Formats", value: "4K, 1080p, 720p" },
        { label: "First Page Out", value: "Not Applicable" },
        { label: "Power Supply", value: "AC 100-240V, 50/60Hz" },
        { label: "Supported Paper Types", value: "Not Applicable" },
        { label: "Power Consumption", value: "350W (Max), 1.5W (Rest Mode)" },
        { label: "Monthly Duty Cycle", value: "Not Applicable" },
        { label: "Standard Paper Handling", value: "Not Applicable" },
        { label: "Touchscreen", value: "No" },
        { label: "Screen Type", value: "Not Applicable" },
        { label: "Recommended Monthly Volume", value: "Not Applicable" },
        { label: "Standard Interfaces", value: "HDMI, USB-C, USB-A, Ethernet" },
        { label: "Optical Resolution", value: "Not Applicable" },
        { label: "Paper Weight", value: "Not Applicable" },
        { label: "Package Contents", value: "PlayStation 5 Console, DualSense Wireless Controller, Base, HDMI Cable, AC Power Cord, USB Cable, Printed Materials" },
        { label: "Weight", value: "4.5 kg" },
        { label: "Color", value: "White" },
        { label: "Dimensions", value: "390 x 104 x 260 mm" },
        { label: "Warranty", value: "1 year" },
      ],
    },
    {
      _id: "joystick_1",
      img: ps5headset,
      productName: "Sony Joystick",
      price: "49",
      color: "Black",
      badge: true,
      brand: "Sony",
      des: "Sony's official joystick for PlayStation consoles, designed for precise control and an immersive gaming experience.",
      cat: "Accessories",
      pdf: pdf1,
      ficheTech: [
        { label: "Availability", value: "In stock" },
        { label: "Brand", value: "Sony" },
        { label: "Color", value: "Black" },
        { label: "Connectivity", value: "Bluetooth" },
        { label: "Battery Life", value: "Up to 12 hours" },
        { label: "Features", value: "Ergonomic design, Vibration feedback" },
        { label: "Package Contents", value: "Joystick, USB Charging Cable, User Manual" },
        { label: "Weight", value: "300 g" },
        { label: "Dimensions", value: "150 x 100 x 60 mm" },
        { label: "Warranty", value: "1 year" },
      ],
    },
    {
      _id: "vr_headset_1",
      img: headset2,
      productName: "Sony 3D VR Headset",
      price: "299",
      color: "Black",
      badge: true,
      brand: "Sony",
      des: "Sony's cutting-edge 3D VR headset, offering an immersive virtual reality experience with high-resolution displays and advanced motion tracking.",
      cat: "Accessories",
      pdf: pdf1,
      ficheTech: [
        { label: "Availability", value: "In stock" },
        { label: "Brand", value: "Sony" },
        { label: "Color", value: "Black" },
        { label: "Display Resolution", value: "1920 x 1080 per eye" },
        { label: "Field of View", value: "100 degrees" },
        { label: "Connectivity", value: "HDMI, USB" },
        { label: "Features", value: "3D audio, Advanced motion tracking, Ergonomic design" },
        { label: "Package Contents", value: "VR Headset, HDMI Cable, USB Cable, User Manual" },
        { label: "Weight", value: "600 g" },
        { label: "Dimensions", value: "200 x 180 x 100 mm" },
        { label: "Warranty", value: "1 year" },
      ],
    },
    {
      _id: "sony_screen_1",
      img: ps5sipederman,
      productName: "Sony Large Screen for Gaming",
      price: "999",
      color: "Black",
      badge: true,
      brand: "Sony",
      des: "Sony's large screen designed specifically for gaming, featuring 4K resolution, HDR support, and a high refresh rate for a superior gaming experience.",
      cat: "Display",
      pdf: pdf1,
      ficheTech: [
        { label: "Availability", value: "In stock" },
        { label: "Brand", value: "Sony" },
        { label: "Screen Size", value: "55 inches" },
        { label: "Resolution", value: "4K (3840 x 2160)" },
        { label: "Refresh Rate", value: "120 Hz" },
        { label: "Connectivity", value: "HDMI, USB, Ethernet" },
        { label: "Features", value: "HDR, 4K, Low Input Lag, Gaming Mode" },
        { label: "Package Contents", value: "Screen, Remote Control, HDMI Cable, User Manual" },
        { label: "Weight", value: "20 kg" },
        { label: "Dimensions", value: "1230 x 710 x 60 mm" },
        { label: "Warranty", value: "1 year" },
      ],
    },

  // =================== imprimante ricoh =================

  {
    _id: "ps5",
    img: "ps5sony",
    productName: "Sony PlayStation 5",
    price: "499",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "Sony PlayStation 5 Console - Enjoy ultra-fast loading with an ultra-high speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games.",
    cat: "Gaming Console",
    pdf: "pdf1",
    ficheTech: [
      { label: "Availability", value: "In stock" },
      { label: "Model", value: "CFI-1015A" },
      { label: "Brand", value: "Sony" },
      { label: "Destocking", value: "No" },
      { label: "Processor", value: "AMD Ryzen Zen 2" },
      { label: "Graphics", value: "AMD Radeon RDNA 2" },
      { label: "Memory", value: "16GB GDDR6" },
      { label: "Storage", value: "825GB SSD" },
      { label: "Optical Drive", value: "Ultra HD Blu-ray" },
      { label: "Connectivity", value: "USB, HDMI, Ethernet, Wi-Fi 6, Bluetooth 5.1" },
      { label: "Max Resolution", value: "8K" },
      { label: "HDR", value: "Yes" },
      { label: "Ray Tracing", value: "Yes" },
      { label: "Frame Rate", value: "Up to 120fps" },
      { label: "Backward Compatibility", value: "Yes, with PS4 games" },
      { label: "Dimensions", value: "390 x 104 x 260 mm" },
      { label: "Weight", value: "4.5 kg" },
      { label: "Color", value: "White" },
      { label: "Warranty", value: "1 year" },
      {
        label: "Box Contents",
        value: "PlayStation 5 Console, DualSense Wireless Controller, Base, HDMI Cable, AC Power Cord, USB Cable, Instruction Manual, Astro's Playroom (Pre-installed game)"
      },
      { label: "Audio", value: "Tempest 3D AudioTech" },
      { label: "Power Consumption", value: "350W" },
      { label: "Cooling System", value: "Custom Cooling Solution" },
      { label: "PlayStation Plus", value: "Yes, subscription required" }
    ],
},

  {
    _id: "ps5_1",
    img: game,
    productName: "PlayStation 5",
    price: "499",
    color: "White",
    badge: true,
    brand: "Sony",
    des: "The PlayStation 5 (PS5) is a home video game console developed by Sony Interactive Entertainment. The PS5 was announced in 2019 as the successor to the PlayStation 4. It was released on November 12, 2020, in Australia, Japan, South Korea, and North America, and on November 19, 2020, in the rest of the world.",
    cat: "Console",
    pdf: pdf1,
    ficheTech: [
      { label: "Availability", value: "In stock" },
      { label: "Model Number", value: "CFI-1000A01" },
      { label: "Brand", value: "Sony" },
      { label: "Discount", value: "No" },
      { label: "Technology", value: "Custom AMD RDNA 2" },
      { label: "Functions", value: "Gaming, Streaming, Media Playback" },
      { label: "Color Output", value: "Full Color" },
      { label: "Memory", value: "16GB GDDR6" },
      { label: "Bluetooth", value: "Yes" },
      { label: "Features", value: "4K Gaming, HDR, Ray Tracing" },
      { label: "Document Loading", value: "Not Applicable" },
      { label: "Connectors", value: "HDMI, USB-C, USB-A" },
      { label: "Processor Speed", value: "3.5 GHz (variable frequency)" },
      { label: "Borderless Printing", value: "Not Applicable" },
      { label: "Black and White Speed", value: "Not Applicable" },
      { label: "Color Speed", value: "Not Applicable" },
      { label: "Black and White Resolution", value: "Not Applicable" },
      { label: "Color Resolution", value: "Not Applicable" },
      { label: "Printing Resolution", value: "Not Applicable" },
      { label: "Scanner Type", value: "Not Applicable" },
      { label: "Scan Speed", value: "Not Applicable" },
      { label: "Scan Resolution", value: "Not Applicable" },
      { label: "Optimized Scan Resolution", value: "Not Applicable" },
      { label: "Duplex Printing", value: "Not Applicable" },
      { label: "Connectivity", value: "Wi-Fi, Ethernet, Bluetooth" },
      { label: "Formats", value: "4K, 1080p, 720p" },
      { label: "First Page Out", value: "Not Applicable" },
      { label: "Power Supply", value: "AC 100-240V, 50/60Hz" },
      { label: "Supported Paper Types", value: "Not Applicable" },
      { label: "Power Consumption", value: "350W (Max), 1.5W (Rest Mode)" },
      { label: "Monthly Duty Cycle", value: "Not Applicable" },
      { label: "Standard Paper Handling", value: "Not Applicable" },
      { label: "Touchscreen", value: "No" },
      { label: "Screen Type", value: "Not Applicable" },
      { label: "Recommended Monthly Volume", value: "Not Applicable" },
      { label: "Standard Interfaces", value: "HDMI, USB-C, USB-A, Ethernet" },
      { label: "Optical Resolution", value: "Not Applicable" },
      { label: "Paper Weight", value: "Not Applicable" },
      { label: "Package Contents", value: "PlayStation 5 Console, DualSense Wireless Controller, Base, HDMI Cable, AC Power Cord, USB Cable, Printed Materials" },
      { label: "Weight", value: "4.5 kg" },
      { label: "Color", value: "White" },
      { label: "Dimensions", value: "390 x 104 x 260 mm" },
      { label: "Warranty", value: "1 year" },
    ],
  },
];
