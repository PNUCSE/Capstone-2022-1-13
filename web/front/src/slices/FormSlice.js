import { createSlice } from '@reduxjs/toolkit'

const initialState = { video: null, logoImage: null }

const formSlice = createSlice({
    name: 'forms',
    initialState,
    reducers: {
        videoAdd: (state, action) => {
            state.video = action.payload.video;
        },
        logoAdd: (state, action) => {
            state.logoImage = action.payload.logoImage
        }
    }
});

const { actions, reducer } = formSlice;

export const { videoAdd, logoAdd } = actions;
export default reducer;