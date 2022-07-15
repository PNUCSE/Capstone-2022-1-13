import React from 'react';
import styles from './TimeStampButton.module.scss';
import classNames from 'classnames/bind';

import { timeMove } from '@/slices/VideoSlice';
import { useDispatch } from 'react-redux';

const TimeStampButton = ({item}) => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();

    const onTimeMove = () => {
        const time = item.start;
        dispatch(timeMove({time}));
    }

    return (
        <>
            <button onClick={onTimeMove}>
                <div className={cx('Button')}>
                    <p>{item.start}</p>
                    <p>~</p>
                    <p>{item.end}</p>
                </div>
            </button>
        </>
    )
}

export default TimeStampButton;