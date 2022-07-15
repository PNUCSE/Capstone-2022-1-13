import React from 'react';
import { useSelector } from 'react-redux';
import TimeStampButton from './TimeStampButton/TimeStampButton';

import classNames from 'classnames/bind';
import styles from './TimeStampContainer.module.scss'

const TimeStampContainer = () => {
    const { result } = useSelector((state) => state.forms)
    const cx = classNames.bind(styles);

    return (
        <div className={cx('Container')}>
            <p>timestamp buttons</p>
            { result.map((item, index) => {
                return <TimeStampButton item={item} key={index}/>
            })}
        </div>
    );
}

export default TimeStampContainer;