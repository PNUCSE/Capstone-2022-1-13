import { createSlice } from '@reduxjs/toolkit'

const initialState = { 
    time: '00:00:00',
    changeToggle: true
}

const videoSlice = createSlice({
    name: 'videos',
    initialState,
    reducers: {
        timeMove: (state, action) => {
            state.time = action.payload.time;
            state.changeToggle = !state.changeToggle;
        }
    }
});

const { actions, reducer } = videoSlice;

export const { timeMove } = actions;
export default reducer;