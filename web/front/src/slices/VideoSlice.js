import { createSlice } from '@reduxjs/toolkit'

const initialState = { 
    time: null
}

const videoSlice = createSlice({
    name: 'videos',
    initialState,
    reducers: {
        timeMove: (state, action) => {
            state.time = action.payload.time;
        }
    }
});

const { actions, reducer } = videoSlice;

export const { timeMove } = actions;
export default reducer;