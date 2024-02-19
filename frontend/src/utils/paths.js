import AccountPage from "../pages/AccountPage/AccountPage";
import HomePage from "../pages/HomePage/HomePage";
import LoginPage from "../pages/LoginPage/LoginPage";
import LogoutPage from "../pages/LogoutPage/LogoutPage";
import RegisterPage from "../pages/RegisterPage/RegisterPage";


const paths = [
    {path: '/', component: HomePage, name: 'Home', exact: true,},
    {path: '/register', component: RegisterPage, name: 'Register', exact: true},
    {path: '/login', component: LoginPage, name: 'Login', exact: true},
    {path: '/account', component: AccountPage, name: 'Account', exact: true},
    {path: '/logout', component: LogoutPage, name: 'Logout', exact: true},
  ];

export default paths;