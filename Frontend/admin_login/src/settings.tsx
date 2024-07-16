interface IDomain {
    testing: "http://127.0.0.1:5000", // Flask Application Domain
    production: "", // If it is integrated to flask application
}


const DOMAIN: IDomain = {
    testing: "http://127.0.0.1:5000",
    production: "",
}


type TProject = 'testing' | 'production'

export const project: TProject = 'testing' // For Development value `testing`, Otherwise `production` before running build.

type TMedia = "/src/images" | "/images"

export const MEDIASRC: TMedia = project === 'testing' ? "/src/images" : "/images";

export default DOMAIN[project];