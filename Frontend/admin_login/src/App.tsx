import { RouterProvider } from "react-router-dom"
import router from "./pages/routes"

function App(): JSX.Element {
    return (
        <div className="main">
            <RouterProvider router={router} />
        </div>
    )
}


export default App;