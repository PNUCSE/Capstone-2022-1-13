import React from 'react'
import PageTemplate from '@/components/common/PageTemplate';
import { VideoForm, LogoForm } from '@/components/form';

const Home = () => {
    return (
        <PageTemplate>
            <VideoForm/>
            <LogoForm/>
        </PageTemplate>
    )
};

export default Home;