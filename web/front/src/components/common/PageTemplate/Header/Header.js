import React from 'react';
import styles from './Header.module.scss';
import classNames from 'classnames/bind';

import { Link } from 'react-router-dom';

const cx = classNames.bind(styles);

const Header = ({route}) => {
    return (
        <header className={cx('Header')}>
            <div className={cx('Header-Content')}>
                <Link to={"/"}>LogoFinder</Link>
                { route &&  
                    <Link to={"."}> / {route}</Link>
                }
            </div>
        </header>
    )
};

export default Header;