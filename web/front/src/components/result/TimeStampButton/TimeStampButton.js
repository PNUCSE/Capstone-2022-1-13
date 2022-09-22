import React from 'react';
import styles from './TimeStampButton.module.scss';
import classNames from 'classnames/bind';

import { timeMove } from '@/slices/VideoSlice';
import { useDispatch, useSelector } from 'react-redux';

const TimeStampButton = ({item}) => {
    const cx = classNames.bind(styles);
    const dispatch = useDispatch();

    const { logoImage } = useSelector((state) => state.forms);

    const onTimeMove = () => {
        const time = item.start;
        dispatch(timeMove({time}));
    }

    const getStringTime = (time) => {
        var timeString = time.substring(0, 7)

        return timeString;
    }

    return (
        <>
            <button onClick={onTimeMove} className={cx('Button')}>
                <img src={URL.createObjectURL(logoImage)} className={cx('LogoImage')}/>
                <div className={cx('TimeDescript')}>
                    <div>{getStringTime(item.start)}</div>
                    <div>&nbsp;~&nbsp;</div>
                    <div>{getStringTime(item.end)}</div>
                </div>
            </button>
        </>
    )
}

export default TimeStampButton;