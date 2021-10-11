import { FunctionComponent } from 'react'

interface VinylProps {
  title: string
  artist: string
  image: string
  price: number
  description: string
}


export const CardView: FunctionComponent<VinylProps> = ({title, artist, image, price, description}) => {
  return (
    <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-4 mb-12">
    <article>
        <section className="mt-6 grid grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-x-6 gap-y-8">
            <article className="relative w-full h-64 bg-cover bg-center group rounded-lg overflow-hidden shadow-lg hover:shadow-2xl  transition duration-300 ease-in-out"
                style={{
                  backgroundImage: `url(${image})`
                }}>
                <div className="absolute inset-0 bg-black bg-opacity-50 group-hover:opacity-75 transition duration-300 ease-in-out"></div>
                <div className="relative w-full h-full px-4 sm:px-6 lg:px-4 flex justify-center items-center">
                    <h3 className="text-center">
                        <a className="text-white text-2xl font-bold text-center" href="#">
                            <span className="absolute inset-0"></span>
                            description
                        </a>
                    </h3>
                </div>
            </article>
        </section>
    </article>
</section>
  )
}