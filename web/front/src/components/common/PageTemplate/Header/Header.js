import React from 'react';
import styles from './Header.module.scss';
import classNames from 'classnames/bind';

const cx = classNames.bind(styles);

const Header = () => {
    return (
        <header className={cx('Header')}>
            <div className={cx('Header-Content')}>
                <div className={cx('breadcomb')}>
                    LogoFinder
                </div>
            </div>
        </header>
    )
};

export default Header;