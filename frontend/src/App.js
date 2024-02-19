import { Route, Routes } from "react-router-dom";
import paths from "./utils/paths";

function App() {
  return (
    <Routes>
      { paths.map( route => 
          <Route key={'{path}'} path={route.path} element={<route.component/>}/>)
      }
    </Routes>
  );
}

export default App;
