import type { NextPage } from 'next'
import Image from 'next/image'
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import { useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import { vinylUrl } from '../env'
import { CardView } from '../components/card'
// import './api/vinyl'

interface VinylInfo {
  artist: string
  cover: URL
  created_at: {
    date: number
  }
  price: string
  title: string
  url: URL
}

interface VinylResponse {
  last: {
    date: number
  }, 
  vinyls: Array<VinylInfo>
}

const Home: NextPage = () => {
  useEffect(() => {
    getVinylInfo()
    // renderVinyl()
  }, []) // TODO: page end or not flag 로 값 바뀔때마다 불러오는건어떨까.
  const [vinylInfoForPage, setVinylInfoForPage] = useState<VinylResponse>({
    last: {date: 0}, vinyls: []
  })

  const getVinylInfo = async () => {
    if (!vinylUrl) {
      console.log('not vinyl url')
      return
    }
    const vinyls = await fetch(vinylUrl, {
      method: 'GET',
    })
    const vinylInfo = await vinyls.json() as VinylResponse
    setVinylInfoForPage(vinylInfo)
  } 

  return (
    <div className={styles.container}>
      <Head>
        <title>Vinyl Trends</title>
        <meta name="description" content="Trends of Japanese vinyl store" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className='md:container md:mx-auto' style={{
          backgroundColor: '#c4c4c4'
        }}>
          {vinylInfoForPage.vinyls.map((vinyl, index) => {
            return (
              <CardView
                key={index}
                artist={vinyl.artist}
                cover={vinyl.cover}
                price={vinyl.price}
                title={vinyl.title}
                url={vinyl.url}
              />
            )
          })}
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://github.com/dev4hobby/amazon-japan-vinyl-alert"
          target="#amazon-japan-vinyl-alert"
          rel="noopener noreferrer"
        >
          d3fau1t: amazon-japan-vinyl-alert
        </a>
      </footer>
    </div>
  )
}

export default Home
